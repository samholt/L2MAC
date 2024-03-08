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
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['profile_picture'] = data['profile_picture']
	return {'message': 'Profile picture updated'}, 200

@app.route('/users/<email>/status', methods=['POST'])
def set_status(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['status'] = data['status']
	user['status_visibility'] = data['visibility']
	return {'message': 'Status updated'}, 200

@app.route('/users/<email>/status/visibility', methods=['POST'])
def set_status_visibility(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['status_visibility'] = data['visibility']
	return {'message': 'Status visibility updated'}, 200

@app.route('/users/<email>/online_status', methods=['POST'])
def set_online_status(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['online_status'] = data['online_status']
	return {'message': 'Online status updated'}, 200

@app.route('/users/<email>/send_message', methods=['POST'])
def send_message(email):
	data = request.get_json()
	receiver = users_db.get(data['receiver_email'])
	if not receiver:
		return {'message': 'Receiver not found'}, 404
	if receiver['online_status'] == 'offline':
		receiver['message_queue'].append({'sender': email, 'message': data['message']})
		return {'message': 'Message queued'}, 200
	else:
		receiver['messages'].append({'sender': email, 'message': data['message']})
		return {'message': 'Message sent'}, 200

# Rest of the code...
