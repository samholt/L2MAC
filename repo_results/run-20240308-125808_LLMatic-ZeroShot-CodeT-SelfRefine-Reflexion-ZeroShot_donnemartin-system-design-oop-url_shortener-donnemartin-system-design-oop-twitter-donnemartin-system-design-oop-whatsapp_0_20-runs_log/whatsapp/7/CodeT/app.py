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

@app.route('/users/<user_id>/profile', methods=['PUT'])
def update_profile(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		user.update_profile(data)
		return jsonify(user.to_dict()), 200
	return {'message': 'User not found'}, 404

@app.route('/users/<user_id>/contacts', methods=['POST'])
def block_unblock_contact(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user:
		user.block_unblock_contact(data)
		return jsonify(user.to_dict()), 200
	return {'message': 'User not found'}, 404

@app.route('/chats', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'], data['participants'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

@app.route('/chats/<chat_id>', methods=['PUT'])
def update_chat(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if chat:
		chat.update(data)
		return jsonify(chat.to_dict()), 200
	return {'message': 'Chat not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
