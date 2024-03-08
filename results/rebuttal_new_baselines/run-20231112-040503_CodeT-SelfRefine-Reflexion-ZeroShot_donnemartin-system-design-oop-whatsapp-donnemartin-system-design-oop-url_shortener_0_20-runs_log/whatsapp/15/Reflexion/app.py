from flask import Flask, request, jsonify
from dataclasses import dataclass
import datetime

app = Flask(__name__)

users = {}
chats = {}

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	last_seen: datetime.datetime
	blocked_users: list
	groups: list

@dataclass
class Chat:
	id: str
	users: list
	messages: list

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	new_user = User(**data)
	users[new_user.id] = new_user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	new_chat = Chat(**data)
	chats[new_chat.id] = new_chat
	return jsonify({'message': 'Chat created successfully'}), 201

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	chat_id = data['chat_id']
	message = data['message']
	chats[chat_id].messages.append(message)
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/view_messages', methods=['GET'])
def view_messages():
	chat_id = request.args.get('chat_id')
	messages = chats[chat_id].messages
	return jsonify({'messages': messages}), 200

if __name__ == '__main__':
	app.run(debug=True)
