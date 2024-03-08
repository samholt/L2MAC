from flask import Flask, request

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = data
	return {'message': 'User created'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/user/<email>/recover', methods=['GET'])
def recover_password(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return {'message': 'Password recovery email sent'}, 200

@app.route('/user/<email>/profile_picture', methods=['POST'])
def set_profile_picture(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['profile_picture'] = data['profile_picture']
	return {'message': 'Profile picture updated'}, 200

@app.route('/user/<email>/status_message', methods=['POST'])
def set_status_message(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['status_message'] = data['status_message']
	return {'message': 'Status message updated'}, 200

@app.route('/user/<email>/privacy_settings', methods=['POST'])
def set_privacy_settings(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['privacy_settings'] = data['privacy_settings']
	return {'message': 'Privacy settings updated'}, 200

@app.route('/user/<email>/block', methods=['POST'])
def block_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'] = user.get('blocked_contacts', [])
	user['blocked_contacts'].append(data['contact_email'])
	return {'message': 'Contact blocked'}, 200

@app.route('/user/<email>/unblock', methods=['POST'])
def unblock_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'] = user.get('blocked_contacts', [])
	if data['contact_email'] in user['blocked_contacts']:
		user['blocked_contacts'].remove(data['contact_email'])
	return {'message': 'Contact unblocked'}, 200

@app.route('/user/<email>/group', methods=['POST'])
def manage_group(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['groups'] = user.get('groups', {})
	user['groups'][data['group_name']] = data['group_members']
	return {'message': 'Group updated'}, 200
