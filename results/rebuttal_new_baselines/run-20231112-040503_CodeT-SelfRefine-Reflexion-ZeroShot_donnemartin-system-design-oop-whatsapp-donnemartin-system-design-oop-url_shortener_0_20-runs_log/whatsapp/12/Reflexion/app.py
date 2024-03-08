from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

users = {}
chats = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = ''
	status_message: str = ''
	contacts: list = []

@dataclass
class Chat:
	id: int
	members: list
	messages: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return {'status': 'User created'}, 201

@app.route('/create_chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(**data)
	chats[chat.id] = chat
	return {'status': 'Chat created'}, 201

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	chat_id = data['chat_id']
	message = data['message']
	chats[chat_id].messages.append(message)
	return {'status': 'Message sent'}, 201

if __name__ == '__main__':
	app.run(debug=True)
