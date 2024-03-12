from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
chats = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@dataclass
class Chat:
	name: str
	members: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/join_chat', methods=['POST'])
def join_chat():
	data = request.get_json()
	chat = chats.get(data['chat_name'])
	if not chat:
		return jsonify({'message': 'Chat not found'}), 404
	chat.members.append(data['user_email'])
	return jsonify({'message': 'User joined chat successfully'}), 200

@app.route('/leave_chat', methods=['POST'])
def leave_chat():
	data = request.get_json()
	chat = chats.get(data['chat_name'])
	if not chat:
		return jsonify({'message': 'Chat not found'}), 404
	chat.members.remove(data['user_email'])
	return jsonify({'message': 'User left chat successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
