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
		if user.email == data['email'] and user.check_password(data['password']):
			return jsonify(user.to_dict()), 200
	return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email']:
			user.reset_password()
			return jsonify({'message': 'Password reset'}), 200
	return jsonify({'error': 'Email not found'}), 404

@app.route('/users/<user_id>/profile', methods=['GET', 'PUT'])
def user_profile(user_id):
	user = users.get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
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
		return jsonify({'error': 'User not found'}), 404
	blocked_user = users.get(data['blocked_user_id'])
	if not blocked_user:
		return jsonify({'error': 'Blocked user not found'}), 404
	user.block_user(blocked_user)
	return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>/unblock', methods=['POST'])
def unblock_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	unblocked_user = users.get(data['unblocked_user_id'])
	if not unblocked_user:
		return jsonify({'error': 'Unblocked user not found'}), 404
	user.unblock_user(unblocked_user)
	return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>/chats', methods=['POST'])
def create_chat(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	chat = Chat(user)
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_chat(chat_id):
	chat = chats.get(chat_id)
	if not chat:
		return jsonify({'error': 'Chat not found'}), 404
	if request.method == 'GET':
		return jsonify(chat.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		chat.update_chat(data)
		return jsonify(chat.to_dict()), 200
	elif request.method == 'DELETE':
		del chats[chat_id]
		return jsonify({'message': 'Chat deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
