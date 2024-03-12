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
	return jsonify({'error': 'Invalid credentials. Please check your email and password.'}), 401

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chat/<chat_id>/message', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return jsonify({'error': 'Chat not found. Please check the chat ID.'}), 404
	message = chat.send_message(data['user_id'], data['content'])
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
