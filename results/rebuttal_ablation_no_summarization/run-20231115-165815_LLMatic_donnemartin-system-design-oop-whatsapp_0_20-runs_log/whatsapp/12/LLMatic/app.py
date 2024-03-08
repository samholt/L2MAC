from flask import Flask, request

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = {'email': data['email'], 'blocked_contacts': [], 'groups': [], 'messages': [], 'statuses': [], 'status_visibility': 'public', 'online': True, 'message_queue': []}
	return {'message': 'User created'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/user/<email>/block', methods=['POST'])
def block_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].append(data['contact_email'])
	return {'message': 'Contact blocked'}, 200

@app.route('/user/<email>/unblock', methods=['POST'])
def unblock_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].remove(data['contact_email'])
	return {'message': 'Contact unblocked'}, 200

@app.route('/user/<email>/group', methods=['POST'])
def create_group(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['groups'].append({'group_name': data['group_name'], 'members': data['members'], 'admin': email})
	return {'message': 'Group created'}, 200

@app.route('/user/<email>/group/<group_name>/add', methods=['POST'])
def add_member(email, group_name):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	for group in user['groups']:
		if group['group_name'] == group_name:
			group['members'].append(data['member_email'])
			return {'message': 'Member added'}, 200
	return {'message': 'Group not found'}, 404

@app.route('/user/<email>/group/<group_name>/remove', methods=['POST'])
def remove_member(email, group_name):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	for group in user['groups']:
		if group['group_name'] == group_name:
			group['members'].remove(data['member_email'])
			return {'message': 'Member removed'}, 200
	return {'message': 'Group not found'}, 404

@app.route('/user/<email>/group/<group_name>/admin', methods=['PUT'])
def update_admin(email, group_name):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	for group in user['groups']:
		if group['group_name'] == group_name:
			group['admin'] = data['new_admin_email']
			return {'message': 'Admin updated'}, 200
	return {'message': 'Group not found'}, 404

@app.route('/user/<email>/message', methods=['POST'])
def send_message(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	if user['online']:
		user['messages'].append({'id': data['id'], 'content': data['content'], 'read': False})
		return {'message': 'Message sent'}, 200
	else:
		user['message_queue'].append({'id': data['id'], 'content': data['content'], 'read': False})
		return {'message': 'Message queued'}, 200

@app.route('/user/<email>/message/<message_id>', methods=['PUT'])
def read_message(email, message_id):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	for message in user['messages']:
		if message['id'] == message_id:
			message['read'] = True
			return {'message': 'Message read'}, 200
	return {'message': 'Message not found'}, 404

@app.route('/user/<email>/message/<message_id>/image', methods=['PUT'])
def share_image(email, message_id):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	for message in user['messages']:
		if message['id'] == message_id:
			message['content'] = data['image_data']
			return {'message': 'Image shared'}, 200
	return {'message': 'Message not found'}, 404

@app.route('/user/<email>/status', methods=['POST'])
def post_status(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['statuses'].append({'id': data['id'], 'image_data': data['image_data']})
	return {'message': 'Status posted'}, 200

@app.route('/user/<email>/status_visibility', methods=['PUT'])
def update_status_visibility(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['status_visibility'] = data['visibility']
	return {'message': 'Status visibility updated'}, 200

@app.route('/user/<email>/online', methods=['PUT'])
def update_online_status(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['online'] = data['online']
	if user['online']:
		user['messages'].extend(user['message_queue'])
		user['message_queue'] = []
	return {'message': 'Online status updated'}, 200
