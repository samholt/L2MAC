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
	users[user.id] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			return jsonify(user.to_dict()), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email']:
			user.reset_password()
			return {'message': 'Password reset successful'}, 200
	return {'message': 'Email not found'}, 404

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	user = users.get(user_id)
	if user:
		return jsonify(user.to_dict()), 200
	return {'message': 'User not found'}, 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
	user = users.get(user_id)
	if user:
		data = request.get_json()
		user.update_profile(data)
		return jsonify(user.to_dict()), 200
	return {'message': 'User not found'}, 404

@app.route('/users/<user_id>/block', methods=['POST'])
def block_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		blocked_user = users.get(data['blocked_user_id'])
		if blocked_user:
			user.block_user(blocked_user)
			return {'message': 'User blocked successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/users/<user_id>/unblock', methods=['POST'])
def unblock_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		unblocked_user = users.get(data['unblocked_user_id'])
		if unblocked_user:
			user.unblock_user(unblocked_user)
			return {'message': 'User unblocked successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'], data['user_ids'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>', methods=['GET'])
def get_chat(chat_id):
	chat = chats.get(chat_id)
	if chat:
		return jsonify(chat.to_dict()), 200
	return {'message': 'Chat not found'}, 404

@app.route('/chats/<chat_id>', methods=['PUT'])
def update_chat(chat_id):
	chat = chats.get(chat_id)
	if chat:
		data = request.get_json()
		chat.update_chat(data)
		return jsonify(chat.to_dict()), 200
	return {'message': 'Chat not found'}, 404

@app.route('/chats/<chat_id>/messages', methods=['POST'])
def send_message(chat_id):
	chat = chats.get(chat_id)
	if chat:
		data = request.get_json()
		message = chat.send_message(data['user_id'], data['content'])
		return jsonify(message), 200
	return {'message': 'Chat not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
