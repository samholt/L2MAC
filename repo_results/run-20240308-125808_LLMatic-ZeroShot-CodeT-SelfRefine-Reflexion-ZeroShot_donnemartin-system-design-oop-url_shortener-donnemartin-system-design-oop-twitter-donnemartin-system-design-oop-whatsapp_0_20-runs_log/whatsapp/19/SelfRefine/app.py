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

@app.route('/users/<user_id>/profile', methods=['GET', 'PUT'])
def user_profile(user_id):
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	if request.method == 'GET':
		return jsonify(user.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.update_profile(data)
		return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>/block', methods=['POST'])
def block_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user_to_block = users.get(data['user_to_block_id'])
	if not user_to_block:
		return {'message': 'User to block not found'}, 404
	user.block_user(user_to_block)
	return {'message': 'User blocked successfully'}, 200

@app.route('/users/<user_id>/unblock', methods=['POST'])
def unblock_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user_to_unblock = users.get(data['user_to_unblock_id'])
	if not user_to_unblock:
		return {'message': 'User to unblock not found'}, 404
	user.unblock_user(user_to_unblock)
	return {'message': 'User unblocked successfully'}, 200

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_chat(chat_id):
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	if request.method == 'GET':
		return jsonify(chat.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		chat.update_chat(data)
		return jsonify(chat.to_dict()), 200
	elif request.method == 'DELETE':
		del chats[chat_id]
		return {'message': 'Chat deleted successfully'}, 200

@app.route('/chats/<chat_id>/add_user', methods=['POST'])
def add_user_to_chat(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	user_to_add = users.get(data['user_to_add_id'])
	if not user_to_add:
		return {'message': 'User to add not found'}, 404
	chat.add_user(user_to_add)
	return {'message': 'User added to chat successfully'}, 200

@app.route('/chats/<chat_id>/remove_user', methods=['POST'])
def remove_user_from_chat(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	user_to_remove = users.get(data['user_to_remove_id'])
	if not user_to_remove:
		return {'message': 'User to remove not found'}, 404
	chat.remove_user(user_to_remove)
	return {'message': 'User removed from chat successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
