from flask import Flask, request, jsonify
from user import User
from chat import Chat
import hashlib

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
	user = User(data['email'], password_hash)
	users[user.email] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
	if data['email'] not in users:
		return {'message': 'User does not exist'}, 404
	elif users[data['email']].password != password_hash:
		return {'message': 'Invalid credentials'}, 401
	else:
		return jsonify(users[data['email']].to_dict()), 200

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	return jsonify(chat.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
