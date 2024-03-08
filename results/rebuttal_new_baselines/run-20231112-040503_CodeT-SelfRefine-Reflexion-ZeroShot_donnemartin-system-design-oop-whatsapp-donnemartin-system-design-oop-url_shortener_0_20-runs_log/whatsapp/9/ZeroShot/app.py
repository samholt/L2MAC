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
	return {'message': 'Invalid credentials'}, 401

@app.route('/users/<user_id>/profile', methods=['PUT'])
def update_profile(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user.update_profile(data)
	return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>/contacts', methods=['POST'])
def block_contact(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	contact = users.get(data['contact_id'])
	if not contact:
		return {'message': 'Contact not found'}, 404
	user.block_contact(contact)
	return jsonify(user.to_dict()), 200

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>/messages', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	user = users.get(data['user_id'])
	if not user:
		return {'message': 'User not found'}, 404
	message = chat.send_message(user, data['content'])
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
