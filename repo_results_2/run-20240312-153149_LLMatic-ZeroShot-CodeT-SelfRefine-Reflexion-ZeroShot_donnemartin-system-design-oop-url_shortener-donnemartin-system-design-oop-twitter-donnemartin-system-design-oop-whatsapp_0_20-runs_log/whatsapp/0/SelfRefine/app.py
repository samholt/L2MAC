from flask import Flask, request, jsonify
from user import User
from chat import Chat

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'error': 'Missing email or password'}), 400
	user = User(data['email'], data['password'])
	users[user.email] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'error': 'Missing email or password'}), 400
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify(user.to_dict()), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	if 'name' not in data:
		return jsonify({'error': 'Missing chat name'}), 400
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chat/<chat_id>/join', methods=['POST'])
def join_chat(chat_id):
	data = request.get_json()
	if 'user_id' not in data:
		return jsonify({'error': 'Missing user ID'}), 400
	chat = chats.get(chat_id)
	if not chat:
		return jsonify({'error': 'Chat not found'}), 404
	chat.join_chat(data['user_id'])
	return jsonify(chat.to_dict()), 200

@app.route('/chat/<chat_id>/message', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	if 'user_id' not in data or 'content' not in data:
		return jsonify({'error': 'Missing user ID or content'}), 400
	chat = chats.get(chat_id)
	if not chat:
		return jsonify({'error': 'Chat not found'}), 404
	if not chat.is_member(data['user_id']):
		return jsonify({'error': 'User not in chat'}), 403
	message = chat.send_message(data['user_id'], data['content'])
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
