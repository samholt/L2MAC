from flask import Flask, request
from models.user import User
from models.chat import Chat

app = Flask(__name__)

users = {}
chats = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = users.get(id)
	if user is None:
		return {'error': 'User not found'}, 404
	return user.__dict__, 200

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(**data)
	chats[chat.id] = chat
	return {'id': chat.id}, 201

@app.route('/chat/<id>', methods=['GET'])
def get_chat(id):
	chat = chats.get(id)
	if chat is None:
		return {'error': 'Chat not found'}, 404
	return chat.__dict__, 200

if __name__ == '__main__':
	app.run(debug=True)
