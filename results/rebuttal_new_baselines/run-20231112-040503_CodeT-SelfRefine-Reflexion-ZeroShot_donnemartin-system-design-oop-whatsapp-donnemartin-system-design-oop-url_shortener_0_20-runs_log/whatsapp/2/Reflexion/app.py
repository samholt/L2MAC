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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], password=data['password'])
	users[user.email] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid email or password'}, 401

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(id=data['id'], users=data['users'], messages=[])
	chats[chat.id] = chat
	return {'message': 'Chat created successfully'}, 201

@app.route('/chats/<int:chat_id>/messages', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if chat and data['user'] in chat.users:
		chat.messages.append(data['message'])
		return {'message': 'Message sent successfully'}, 201
	return {'message': 'Invalid chat or user'}, 400

if __name__ == '__main__':
	app.run(debug=True)
