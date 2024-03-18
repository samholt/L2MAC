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
	return 'Invalid email or password', 401

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email']:
			user.reset_password()
			return 'Password reset successful', 200
	return 'Email not found', 404

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users.get(data['user_id'])
	if user:
		user.update_profile(data['profile_picture'], data['status_message'])
		return jsonify(user.to_dict()), 200
	return 'User not found', 404

@app.route('/block_user', methods=['POST'])
def block_user():
	data = request.get_json()
	user = users.get(data['user_id'])
	if user:
		user.block_user(data['blocked_user_id'])
		return 'User blocked', 200
	return 'User not found', 404

@app.route('/unblock_user', methods=['POST'])
def unblock_user():
	data = request.get_json()
	user = users.get(data['user_id'])
	if user:
		user.unblock_user(data['unblocked_user_id'])
		return 'User unblocked', 200
	return 'User not found', 404

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	chat = Chat(data['name'], data['picture'], data['admin_id'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/add_participant', methods=['POST'])
def add_participant():
	data = request.get_json()
	chat = chats.get(data['chat_id'])
	if chat:
		chat.add_participant(data['participant_id'])
		return jsonify(chat.to_dict()), 200
	return 'Chat not found', 404

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	data = request.get_json()
	chat = chats.get(data['chat_id'])
	if chat:
		chat.remove_participant(data['participant_id'])
		return jsonify(chat.to_dict()), 200
	return 'Chat not found', 404

if __name__ == '__main__':
	app.run(debug=True)
