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

@app.route('/users/<user_id>/chats', methods=['POST'])
def create_chat(user_id):
	data = request.get_json()
	chat = Chat(data['name'])
	chat.add_user(users[user_id])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
