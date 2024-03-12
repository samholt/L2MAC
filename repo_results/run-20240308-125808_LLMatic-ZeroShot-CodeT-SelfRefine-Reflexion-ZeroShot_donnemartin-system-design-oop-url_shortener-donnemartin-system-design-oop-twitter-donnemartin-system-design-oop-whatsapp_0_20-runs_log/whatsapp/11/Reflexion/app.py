from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

users = {}
chats = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@dataclass
class Chat:
	id: int
	users: list
	messages: list

@dataclass
class Message:
	user: User
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['name'], data['email'], data['password'])
	users[user.email] = user
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid email or password'}, 400

@app.route('/create_chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(len(chats), data['users'], [])
	chats[chat.id] = chat
	return {'message': 'Chat created successfully'}, 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	chat = chats.get(data['chat_id'])
	user = users.get(data['email'])
	if chat and user:
		message = Message(user, data['content'])
		chat.messages.append(message)
		return {'message': 'Message sent successfully'}, 200
	return {'message': 'Invalid chat or user'}, 400

if __name__ == '__main__':
	app.run(debug=True)
