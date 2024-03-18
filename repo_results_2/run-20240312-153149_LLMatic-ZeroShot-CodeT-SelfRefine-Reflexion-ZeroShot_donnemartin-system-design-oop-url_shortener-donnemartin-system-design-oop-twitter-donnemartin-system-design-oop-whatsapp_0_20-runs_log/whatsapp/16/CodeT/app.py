from flask import Flask, request
from user import User
from chat import Chat

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			return {'id': user.id}, 200
	return {'error': 'Invalid credentials'}, 401

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return {'id': chat.id}, 201

@app.route('/chat/<chat_id>/message', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats[chat_id]
	chat.send_message(data['user_id'], data['message'])
	return {}, 204

if __name__ == '__main__':
	app.run(debug=True)
