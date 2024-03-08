from flask import Flask, request
import hashlib

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = data
	return {'message': 'User created'}, 201

@app.route('/users/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/users/<email>/recover', methods=['POST'])
def recover_password(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return {'message': 'Password recovery email sent'}, 200

@app.route('/users/<email>/profile_picture', methods=['POST'])
def set_profile_picture(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	data = request.get_json()
	user['profile_picture'] = data['profile_picture']
	return {'message': 'Profile picture updated'}, 200

@app.route('/users/<email>/status_message', methods=['POST'])
def set_status_message(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	data = request.get_json()
	user['status_message'] = data['status_message']
	return {'message': 'Status message updated'}, 200

@app.route('/users/<email>/privacy_settings', methods=['POST'])
def set_privacy_settings(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	data = request.get_json()
	user['privacy_settings'] = data['privacy_settings']
	return {'message': 'Privacy settings updated'}, 200

@app.route('/users/<email>/block', methods=['POST'])
def block_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].append(data['blocked_email'])
	return {'message': 'Contact blocked'}, 200

@app.route('/users/<email>/unblock', methods=['POST'])
def unblock_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].remove(data['unblocked_email'])
	return {'message': 'Contact unblocked'}, 200

@app.route('/users/<email>/groups', methods=['POST'])
def manage_groups(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['groups'][data['group_name']] = data['contacts']
	return {'message': 'Group updated'}, 200

@app.route('/message/send', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = users_db.get(data['sender_email'])
	receiver = users_db.get(data['receiver_email'])
	if not sender or not receiver:
		return {'message': 'User not found'}, 404
	message = {'sender': data['sender_email'], 'receiver': data['receiver_email'], 'message': data['message'], 'read': False}
	sender['messages'].append(message)
	receiver['messages'].append(message)
	return {'message': 'Message sent'}, 200

@app.route('/message/read', methods=['POST'])
def read_message():
	data = request.get_json()
	user = users_db.get(data['email'])
	if not user:
		return {'message': 'User not found'}, 404
	for message in user['messages']:
		if message['sender'] == data['sender_email'] and message['message'] == data['message']:
			message['read'] = True
	return {'message': 'Message marked as read'}, 200

@app.route('/message/encrypt', methods=['POST'])
def encrypt_message():
	data = request.get_json()
	encrypted_message = hashlib.sha256(data['message'].encode()).hexdigest()
	return {'encrypted_message': encrypted_message}, 200

@app.route('/message/share_image', methods=['POST'])
def share_image():
	data = request.get_json()
	sender = users_db.get(data['sender_email'])
	receiver = users_db.get(data['receiver_email'])
	if not sender or not receiver:
		return {'message': 'User not found'}, 404
	message = {'sender': data['sender_email'], 'receiver': data['receiver_email'], 'image': data['image'], 'read': False}
	sender['messages'].append(message)
	receiver['messages'].append(message)
	return {'message': 'Image shared'}, 200
