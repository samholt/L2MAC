from flask import Flask, jsonify, request
import uuid
import datetime

app = Flask(__name__)

users = {}
messages = {}
groups = {}
statuses = {}

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user_id = str(uuid.uuid4())
	users[user_id] = data
	users[user_id]['blocked_contacts'] = []
	users[user_id]['groups'] = []
	return jsonify({'user_id': user_id}), 201

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user_id = data.get('user_id')
	if user_id in users:
		email = users[user_id]['email']
		print(f'Send password reset link to {email}')
		return jsonify({'message': 'Password reset link sent.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	user_id = data.get('user_id')
	new_picture = data.get('new_picture')
	if user_id in users:
		users[user_id]['profile_picture'] = new_picture
		return jsonify({'message': 'Profile picture updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	user_id = data.get('user_id')
	new_status = data.get('new_status')
	if user_id in users:
		users[user_id]['status_message'] = new_status
		return jsonify({'message': 'Status message updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/update_privacy_settings', methods=['POST'])
def update_privacy_settings():
	data = request.get_json()
	user_id = data.get('user_id')
	new_settings = data.get('new_settings')
	if user_id in users:
		users[user_id]['privacy_settings'] = new_settings
		return jsonify({'message': 'Privacy settings updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user_id = data.get('user_id')
	contact_id = data.get('contact_id')
	if user_id in users and contact_id in users:
		users[user_id]['blocked_contacts'].append(contact_id)
		return jsonify({'message': 'Contact blocked.'}), 200
	else:
		return jsonify({'message': 'User or contact not found.'}), 404

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user_id = data.get('user_id')
	contact_id = data.get('contact_id')
	if user_id in users and contact_id in users:
		if contact_id in users[user_id]['blocked_contacts']:
			users[user_id]['blocked_contacts'].remove(contact_id)
			return jsonify({'message': 'Contact unblocked.'}), 200
		else:
			return jsonify({'message': 'Contact not blocked.'}), 404
	else:
		return jsonify({'message': 'User or contact not found.'}), 404

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	group_id = str(uuid.uuid4())
	group_name = data.get('group_name')
	admin_id = data.get('admin_id')
	if admin_id in users:
		groups[group_id] = {'group_name': group_name, 'admin_id': admin_id, 'members': [admin_id]}
		users[admin_id]['groups'].append(group_id)
		return jsonify({'message': 'Group created.', 'group_id': group_id}), 201
	else:
		return jsonify({'message': 'Admin user not found.'}), 404

@app.route('/manage_group', methods=['POST'])
def manage_group():
	data = request.get_json()
	user_id = data.get('user_id')
	group_id = data.get('group_id')
	action = data.get('action')
	if user_id in users and group_id in groups:
		if action == 'add':
			if user_id not in groups[group_id]['members']:
				groups[group_id]['members'].append(user_id)
				users[user_id]['groups'].append(group_id)
				return jsonify({'message': 'User added to group.'}), 200
			else:
				return jsonify({'message': 'User already in group.'}), 400
		elif action == 'remove':
			if user_id in groups[group_id]['members']:
				groups[group_id]['members'].remove(user_id)
				users[user_id]['groups'].remove(group_id)
				return jsonify({'message': 'User removed from group.'}), 200
			else:
				return jsonify({'message': 'User not in group.'}), 404
		elif action == 'promote':
			if user_id == groups[group_id]['admin_id']:
				new_admin_id = data.get('new_admin_id')
				if new_admin_id in groups[group_id]['members']:
					groups[group_id]['admin_id'] = new_admin_id
					return jsonify({'message': 'User promoted to admin.'}), 200
				else:
					return jsonify({'message': 'New admin not in group.'}), 404
			else:
				return jsonify({'message': 'Only the group admin can promote a new admin.'}), 403
	else:
		return jsonify({'message': 'User or group not found.'}), 404

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	conversation_id = data.get('conversation_id')
	sender_id = data.get('sender_id')
	message_content = data.get('message_content')
	message_type = data.get('message_type')
	if conversation_id not in messages:
		messages[conversation_id] = []
	message = {'sender_id': sender_id, 'content': message_content, 'type': message_type, 'read': False}
	messages[conversation_id].append(message)
	return jsonify({'message': 'Message sent.'}), 200

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	conversation_id = data.get('conversation_id')
	message_index = data.get('message_index')
	if conversation_id in messages and message_index < len(messages[conversation_id]):
		messages[conversation_id][message_index]['read'] = True
		return jsonify({'message': 'Message marked as read.'}), 200
	else:
		return jsonify({'message': 'Message not found.'}), 404

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user_id = data.get('user_id')
	image = data.get('image')
	visibility = data.get('visibility')
	expiry_time = datetime.datetime.strptime(data.get('expiry_time'), '%Y-%m-%d %H:%M:%S.%f')
	if user_id in users:
		if user_id not in statuses:
			statuses[user_id] = []
		status = {'image': image, 'visibility': visibility, 'expiry_time': expiry_time}
		statuses[user_id].append(status)
		return jsonify({'message': 'Status posted.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/get_statuses', methods=['GET'])
def get_statuses():
	user_id = request.args.get('user_id')
	if user_id in statuses:
		valid_statuses = [status for status in statuses[user_id] if datetime.datetime.now() < status['expiry_time']]
		return jsonify(valid_statuses), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

if __name__ == '__main__':
	app.run(debug=True)

