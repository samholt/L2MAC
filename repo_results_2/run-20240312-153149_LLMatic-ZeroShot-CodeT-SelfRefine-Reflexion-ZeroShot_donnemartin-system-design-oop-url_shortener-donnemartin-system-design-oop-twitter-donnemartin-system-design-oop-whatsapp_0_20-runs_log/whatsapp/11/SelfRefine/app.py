from flask import Flask, request, jsonify
from user import User
from chat import Chat
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	user = User(data['email'], hashed_password)
	users[user.email] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and check_password_hash(user.password, data['password']):
		return jsonify(user.to_dict()), 200
	elif not user:
		return {'message': 'User not found'}, 404
	else:
		return {'message': 'Invalid credentials'}, 401

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
		return {'message': 'Chat not found'}, 404
	message = chat.send_message(data['user_id'], data['content'])
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
