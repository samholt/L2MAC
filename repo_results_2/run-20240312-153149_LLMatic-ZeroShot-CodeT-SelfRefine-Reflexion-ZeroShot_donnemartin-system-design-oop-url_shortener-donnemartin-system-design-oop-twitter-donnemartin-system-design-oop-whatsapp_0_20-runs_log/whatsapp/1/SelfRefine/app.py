from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from user import User
from chat import Chat

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(email=data['email'], password=data['password'])
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

@app.route('/users/<user_id>/contacts', methods=['GET', 'POST'])
def contacts(user_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	if request.method == 'GET':
		return jsonify([contact.to_dict() for contact in user.contacts]), 200
	elif request.method == 'POST':
		data = request.get_json()
		contact = users.get(data['contact_id'])
		if not contact:
			return 'Contact not found', 404
		user.add_contact(contact)
		return jsonify(contact.to_dict()), 201

@app.route('/users/<user_id>/contacts/<contact_id>', methods=['DELETE'])
def delete_contact(user_id, contact_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	contact = users.get(contact_id)
	if not contact:
		return 'Contact not found', 404
	user.remove_contact(contact)
	return 'Contact removed', 200

@app.route('/users/<user_id>/chats', methods=['GET', 'POST'])
def chats(user_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	if request.method == 'GET':
		return jsonify([chat.to_dict() for chat in user.chats]), 200
	elif request.method == 'POST':
		data = request.get_json()
		chat = Chat(name=data['name'])
		chats[chat.id] = chat
		user.add_chat(chat)
		return jsonify(chat.to_dict()), 201

@app.route('/users/<user_id>/chats/<chat_id>', methods=['GET', 'PUT', 'DELETE'])
def chat(user_id, chat_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	chat = chats.get(chat_id)
	if not chat:
		return 'Chat not found', 404
	if request.method == 'GET':
		return jsonify(chat.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		chat.update(data)
		return jsonify(chat.to_dict()), 200
	elif request.method == 'DELETE':
		user.remove_chat(chat)
		return 'Chat deleted', 200

if __name__ == '__main__':
	app.run(debug=True)
