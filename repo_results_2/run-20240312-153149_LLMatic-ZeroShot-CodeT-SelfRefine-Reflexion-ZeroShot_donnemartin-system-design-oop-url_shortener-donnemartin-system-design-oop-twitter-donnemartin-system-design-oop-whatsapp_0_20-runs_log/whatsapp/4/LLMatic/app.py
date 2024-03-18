from flask import Flask, request
import base64

app = Flask(__name__)

# Mock database
users_db = {}
messages_db = []

@app.route('/')
def home():
	return 'Welcome to the Home Page!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	users_db[data['email']] = {
		'password': data['password'],
		'profile_picture': data.get('profile_picture', ''),
		'status_message': data.get('status_message', ''),
		'privacy_settings': data.get('privacy_settings', 'public'),
		'blocked_contacts': [],
		'groups': {}
	}
	return 'User registered successfully!'

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None or user['password'] != data['password']:
		return 'Invalid email or password!', 401
	return 'Logged in successfully!'

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	if data['email'] not in users_db:
		return 'No user with this email!', 404
	# Mock password reset link generation
	reset_link = 'https://example.com/reset_password/' + data['email']
	return reset_link

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None:
		return 'No user with this email!', 404
	user['profile_picture'] = data.get('profile_picture', user['profile_picture'])
	user['status_message'] = data.get('status_message', user['status_message'])
	user['privacy_settings'] = data.get('privacy_settings', user['privacy_settings'])
	return 'Profile updated successfully!'

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None:
		return 'No user with this email!', 404
	user['blocked_contacts'].append(data['contact_email'])
	return 'Contact blocked successfully!'

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None:
		return 'No user with this email!', 404
	user['blocked_contacts'].remove(data['contact_email'])
	return 'Contact unblocked successfully!'

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None:
		return 'No user with this email!', 404
	user['groups'][data['group_name']] = {
		'group_picture': data.get('group_picture', ''),
		'participants': [],
		'admins': [data['email']]
	}
	return 'Group created successfully!'

@app.route('/edit_group', methods=['POST'])
def edit_group():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user is None:
		return 'No user with this email!', 404
	group = user['groups'].get(data['group_name'])
	if group is None:
		return 'No group with this name!', 404
	if data['email'] not in group['admins']:
		return 'Only admins can edit the group!', 403
	group['group_picture'] = data.get('group_picture', group['group_picture'])
	group['participants'].extend(data.get('add_participants', []))
	for participant in data.get('remove_participants', []):
		group['participants'].remove(participant)
	group['admins'].extend(data.get('add_admins', []))
	for admin in data.get('remove_admins', []):
		if admin != data['email']:
			group['admins'].remove(admin)
	return 'Group edited successfully!'

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = {
		'id': len(messages_db),
		'sender': data['sender_email'],
		'recipient': data['recipient_email'],
		'content': base64.b64encode(data['content'].encode()).decode(),
		'read': False
	}
	messages_db.append(message)
	return 'Message sent successfully!'

@app.route('/receive_messages', methods=['GET'])
def receive_messages():
	user_email = request.args.get('email')
	messages = [msg for msg in messages_db if msg['recipient'] == user_email]
	for message in messages:
		message['content'] = base64.b64decode(message['content'].encode()).decode()
	return {'messages': messages}

@app.route('/mark_as_read', methods=['POST'])
def mark_as_read():
	data = request.get_json()
	message = messages_db[data['message_id']]
	message['read'] = True
	return 'Message marked as read!'

@app.route('/send_media', methods=['POST'])
def send_media():
	data = request.get_json()
	message = {
		'id': len(messages_db),
		'sender': data['sender_email'],
		'recipient': data['recipient_email'],
		'content': data['media_content'],
		'read': False
	}
	messages_db.append(message)
	return 'Media sent successfully!'

if __name__ == '__main__':
	app.run(debug=True)
