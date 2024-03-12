from flask import Flask, request
from models.user import User
from models.chat import Chat

app = Flask(__name__)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/user/<user_id>/settings', methods=['PUT'])
def update_user_settings(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user.set_profile_picture(data.get('profile_picture'))
	user.set_status_message(data.get('status_message'))
	user.set_privacy_settings(data.get('privacy_settings'))
	return {'message': 'User settings updated successfully'}, 200

@app.route('/user/<user_id>/block', methods=['POST'])
def block_contact(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user.block_contact(data.get('contact'))
	return {'message': 'Contact blocked successfully'}, 200

@app.route('/user/<user_id>/unblock', methods=['POST'])
def unblock_contact(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user.unblock_contact(data.get('contact'))
	return {'message': 'Contact unblocked successfully'}, 200

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(**data)
	chats[chat.id] = chat
	return {'message': 'Chat created successfully'}, 201

@app.route('/chat/<chat_id>/member', methods=['POST'])
def add_chat_member(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	chat.add_member(data.get('member'))
	return {'message': 'Member added successfully'}, 200

@app.route('/chat/<chat_id>/member', methods=['DELETE'])
def remove_chat_member(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	chat.remove_member(data.get('member'))
	return {'message': 'Member removed successfully'}, 200

@app.route('/chat/<chat_id>/message', methods=['POST'])
def send_message(chat_id):
	data = request.get_json()
	chat = chats.get(chat_id)
	if not chat:
		return {'message': 'Chat not found'}, 404
	chat.send_message(data.get('message'))
	return {'message': 'Message sent successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
