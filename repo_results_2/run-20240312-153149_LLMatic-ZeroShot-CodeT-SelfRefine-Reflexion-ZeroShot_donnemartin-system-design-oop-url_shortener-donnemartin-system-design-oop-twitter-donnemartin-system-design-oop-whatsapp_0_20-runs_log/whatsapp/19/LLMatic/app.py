from flask import Flask, request
import hashlib

app = Flask(__name__)

# Mock database
users_db = {}
messages_db = {}

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

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return {'message': 'Email and password are required'}, 400
	users_db[data['email']] = {'password': data['password'], 'profile_picture': '', 'status_message': '', 'privacy_settings': {'details_visible': True, 'last_seen_visible': True}, 'contacts': [], 'blocked_contacts': [], 'groups': {}}
	return {'message': 'User signed up'}, 201

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = users_db.get(data['email'])
	if not user:
		return {'message': 'User not found'}, 404
	user['password'] = data['new_password']
	return {'message': 'Password updated'}, 200

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
def update_privacy_settings(email):
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
	if data['contact_email'] in user['contacts']:
		user['contacts'].remove(data['contact_email'])
	user['blocked_contacts'].append(data['contact_email'])
	return {'message': 'Contact blocked'}, 200

@app.route('/user/<email>/unblock', methods=['POST'])
def unblock_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	if data['contact_email'] in user['blocked_contacts']:
		user['blocked_contacts'].remove(data['contact_email'])
	user['contacts'].append(data['contact_email'])
	return {'message': 'Contact unblocked'}, 200

@app.route('/user/<email>/group', methods=['POST'])
def create_group(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	group_id = len(user['groups']) + 1
	user['groups'][group_id] = {'name': data['name'], 'picture': data['picture'], 'members': [email], 'admins': [email], 'admin_permissions': {'add_members': True, 'remove_members': True, 'assign_admins': True}}
	return {'message': 'Group created', 'group_id': group_id}, 201

@app.route('/user/<email>/group/<group_id>/assign_admin', methods=['POST'])
def assign_admin(email, group_id):
	data = request.get_json()
	user = users_db.get(email)
	group_id = int(group_id)
	if not user or group_id not in user['groups']:
		return {'message': 'Group not found'}, 404
	group = user['groups'][group_id]
	if email not in group['admins'] or not group['admin_permissions']['assign_admins']:
		return {'message': 'Permission denied'}, 403
	for member_email in data.get('admins', []):
		if member_email in group['members'] and member_email not in group['admins']:
			group['admins'].append(member_email)
	return {'message': 'Admins assigned'}, 200

@app.route('/user/<email>/group/<group_id>/remove_admin', methods=['POST'])
def remove_admin(email, group_id):
	data = request.get_json()
	user = users_db.get(email)
	group_id = int(group_id)
	if not user or group_id not in user['groups']:
		return {'message': 'Group not found'}, 404
	group = user['groups'][group_id]
	if email not in group['admins'] or not group['admin_permissions']['assign_admins']:
		return {'message': 'Permission denied'}, 403
	for member_email in data.get('admins', []):
		if member_email in group['admins']:
			group['admins'].remove(member_email)
	return {'message': 'Admins removed'}, 200

@app.route('/user/<email>/group/<group_id>/set_permissions', methods=['POST'])
def set_permissions(email, group_id):
	data = request.get_json()
	user = users_db.get(email)
	group_id = int(group_id)
	if not user or group_id not in user['groups']:
		return {'message': 'Group not found'}, 404
	group = user['groups'][group_id]
	if email not in group['admins'] or not group['admin_permissions']['assign_admins']:
		return {'message': 'Permission denied'}, 403
	group['admin_permissions'] = data.get('permissions', group['admin_permissions'])
	return {'message': 'Permissions set'}, 200

@app.route('/user/<email>/group/<group_id>', methods=['PUT'])
def update_group(email, group_id):
	data = request.get_json()
	user = users_db.get(email)
	group_id = int(group_id)
	if not user or group_id not in user['groups']:
		return {'message': 'Group not found'}, 404
	group = user['groups'][group_id]
	group['name'] = data.get('name', group['name'])
	group['picture'] = data.get('picture', group['picture'])
	if email in group['admins'] and group['admin_permissions']['add_members']:
		for member_email in data.get('add_members', []):
			if member_email not in group['members']:
				group['members'].append(member_email)
	if email in group['admins'] and group['admin_permissions']['remove_members']:
		for member_email in data.get('remove_members', []):
			if member_email in group['members']:
				group['members'].remove(member_email)
	return {'message': 'Group updated'}, 200

@app.route('/user/<email>/message', methods=['POST'])
def send_message(email):
	data = request.get_json()
	recipient = users_db.get(data['recipient_email'])
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message_id = len(messages_db) + 1
	messages_db[message_id] = {'sender': email, 'recipient': data['recipient_email'], 'message': hashlib.sha256(data['message'].encode()).hexdigest(), 'read': False}
	return {'message': 'Message sent', 'message_id': message_id}, 201

@app.route('/user/<email>/message/<message_id>', methods=['PUT'])
def read_message(email, message_id):
	message_id = int(message_id)
	message = messages_db.get(message_id)
	if not message or message['recipient'] != email:
		return {'message': 'Message not found'}, 404
	message['read'] = True
	return {'message': 'Message marked as read'}, 200

@app.route('/user/<email>/message/image', methods=['POST'])
def send_image(email):
	data = request.get_json()
	recipient = users_db.get(data['recipient_email'])
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message_id = len(messages_db) + 1
	messages_db[message_id] = {'sender': email, 'recipient': data['recipient_email'], 'image': data['image'], 'read': False}
	return {'message': 'Image sent', 'message_id': message_id}, 201

@app.route('/user/<email>/message/emoji', methods=['POST'])
def send_emoji(email):
	data = request.get_json()
	recipient = users_db.get(data['recipient_email'])
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message_id = len(messages_db) + 1
	messages_db[message_id] = {'sender': email, 'recipient': data['recipient_email'], 'emoji': data['emoji'], 'read': False}
	return {'message': 'Emoji sent', 'message_id': message_id}, 201

@app.route('/user/<email>/message/gif', methods=['POST'])
def send_gif(email):
	data = request.get_json()
	recipient = users_db.get(data['recipient_email'])
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message_id = len(messages_db) + 1
	messages_db[message_id] = {'sender': email, 'recipient': data['recipient_email'], 'gif': data['gif'], 'read': False}
	return {'message': 'GIF sent', 'message_id': message_id}, 201

@app.route('/user/<email>/message/sticker', methods=['POST'])
def send_sticker(email):
	data = request.get_json()
	recipient = users_db.get(data['recipient_email'])
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message_id = len(messages_db) + 1
	messages_db[message_id] = {'sender': email, 'recipient': data['recipient_email'], 'sticker': data['sticker'], 'read': False}
	return {'message': 'Sticker sent', 'message_id': message_id}, 201

if __name__ == '__main__':
	app.run(debug=True)
