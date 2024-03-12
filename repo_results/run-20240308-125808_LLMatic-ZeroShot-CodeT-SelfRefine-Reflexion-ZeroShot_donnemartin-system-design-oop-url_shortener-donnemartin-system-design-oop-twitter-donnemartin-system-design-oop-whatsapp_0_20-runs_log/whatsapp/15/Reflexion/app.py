from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
chats = {}

@dataclass
class User:
	id: str
	email: str
	password: str

@dataclass
class Chat:
	id: str
	users: list
	messages: list

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify([user for user in users.values()]), 200

@app.route('/users/<user_id>/chats', methods=['GET'])
def get_user_chats(user_id):
	user_chats = [chat for chat in chats.values() if user_id in chat.users]
	return jsonify(user_chats), 200

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(**data)
	chats[chat.id] = chat
	return jsonify(chat), 201

@app.route('/chats/<chat_id>/messages', methods=['GET'])
def get_chat_messages(chat_id):
	chat = chats.get(chat_id)
	if chat:
		return jsonify(chat.messages), 200
	else:
		return {'error': 'Chat not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
