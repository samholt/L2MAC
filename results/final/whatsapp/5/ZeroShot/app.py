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
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/users/<user_id>/profile', methods=['PUT'])
def update_profile(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		user.update_profile(data)
		return jsonify(user.to_dict()), 200
	return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>/contacts', methods=['POST'])
def add_contact(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		contact = users.get(data['contact_id'])
		if contact:
			user.add_contact(contact)
			return jsonify(user.to_dict()), 200
		return jsonify({'error': 'Contact not found'}), 404
	return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>/chats', methods=['POST'])
def start_chat(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		chat = Chat(user)
		chats[chat.id] = chat
		return jsonify(chat.to_dict()), 201
	return jsonify({'error': 'User not found'}), 404

@app.route('/chats/<chat_id>/messages', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if chat:
		message = chat.send_message(data['sender_id'], data['content'])
		return jsonify(message), 201
	return jsonify({'error': 'Chat not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
