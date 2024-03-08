from flask import Blueprint, request, jsonify
from .models import User, Message

chat = Blueprint('chat', __name__)

# Mock database
users_db = {'user1': User(id=1, username='user1', email='user1@example.com', profile_picture='', status_message='', privacy_settings='', blocked_contacts=[]), 'user2': User(id=2, username='user2', email='user2@example.com', profile_picture='', status_message='', privacy_settings='', blocked_contacts=[]) }
users_db['user1'].set_password('pass1')
users_db['user2'].set_password('pass2')
messages_db = {}

@chat.route('/send', methods=['POST'])
def send_message():
	data = request.get_json()
	from_user = users_db.get(data['from'])
	to_user = users_db.get(data['to'])
	if not from_user or not to_user:
		return jsonify({'message': 'User not found'}), 404
	message = Message(id=len(messages_db)+1, sender=from_user, receiver=to_user, content=data['content'], timestamp=None, read_receipt=False, encryption=False)
	messages_db[message.id] = message
	return jsonify({'message': 'Message sent'}), 200

@chat.route('/receive', methods=['GET'])
def receive_message():
	data = request.args
	user = users_db.get(data['user_id'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	received_messages = [message for message in messages_db.values() if message.receiver == user and not message.read_receipt]
	for message in received_messages:
		if message.encryption:
			message.decrypt_content('encryption_key')
		message.read_receipt = True
	return jsonify({'messages': [message.content for message in received_messages]}), 200

@chat.route('/history', methods=['GET'])
def view_history():
	data = request.args
	user = users_db.get(data['user_id'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	sent_messages = [message for message in messages_db.values() if message.sender == user]
	received_messages = [message for message in messages_db.values() if message.receiver == user]
	return jsonify({'sent_messages': [message.content for message in sent_messages], 'received_messages': [message.content for message in received_messages]}), 200
