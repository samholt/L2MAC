from flask import Flask, request, jsonify
from user import User
from chat import Chat

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	users[user.email] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify(user.to_dict()), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/users/<user_id>/chats', methods=['POST'])
def create_chat(user_id):
	data = request.get_json()
	chat = Chat(data['name'])
	chat.add_user(user_id)
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/users/<user_id>/chats/<chat_id>/messages', methods=['POST'])
def send_message(user_id, chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat or user_id not in chat.users:
		return jsonify({'error': 'User not in chat'}), 403
	message = chat.send_message(user_id, data['content'])
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
