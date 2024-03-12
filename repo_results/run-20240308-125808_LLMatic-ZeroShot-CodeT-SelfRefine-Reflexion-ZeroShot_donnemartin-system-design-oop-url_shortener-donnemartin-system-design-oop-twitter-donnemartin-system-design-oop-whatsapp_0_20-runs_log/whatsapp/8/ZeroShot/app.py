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
			return 'Password reset email sent', 200
	return 'Email not found', 404

@app.route('/users/<user_id>/profile', methods=['GET', 'PUT'])
def profile(user_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	if request.method == 'GET':
		return jsonify(user.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.update_profile(data)
		return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>/contacts', methods=['POST'])
def block_unblock_contact(user_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	data = request.get_json()
	contact = users.get(data['contact_id'])
	if not contact:
		return 'Contact not found', 404
	if data['action'] == 'block':
		user.block_contact(contact)
	elif data['action'] == 'unblock':
		user.unblock_contact(contact)
	return 'Action performed', 200

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>', methods=['GET', 'PUT'])
def manage_chat(chat_id):
	chat = chats.get(chat_id)
	if not chat:
		return 'Chat not found', 404
	if request.method == 'GET':
		return jsonify(chat.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		chat.update_chat(data)
		return jsonify(chat.to_dict()), 200

if __name__ == '__main__':
	app.run(debug=True)
