from flask import Flask, request
import hashlib
import time

app = Flask(__name__)

# Mock database
users = {}
messages = {}
statuses = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/signup', methods=['POST'])
def signup():
	email = request.json.get('email')
	password = request.json.get('password')
	if email in users:
		return 'User already exists', 400
	users[email] = {'password': password, 'profile_picture': '', 'status_message': '', 'privacy_settings': {'details': True, 'last_seen': True}, 'blocked_contacts': [], 'groups': {}}
	return 'User created', 201

@app.route('/login', methods=['POST'])
def login():
	email = request.json.get('email')
	password = request.json.get('password')
	if users.get(email, {}).get('password') != password:
		return 'Invalid credentials', 401
	return 'Logged in', 200

@app.route('/recover', methods=['POST'])
def recover():
	email = request.json.get('email')
	if email not in users:
		return 'User does not exist', 404
	return users[email]['password'], 200

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	email = request.json.get('email')
	profile_picture = request.json.get('profile_picture')
	if email not in users:
		return 'User does not exist', 404
	users[email]['profile_picture'] = profile_picture
	return 'Profile picture updated', 200

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	email = request.json.get('email')
	status_message = request.json.get('status_message')
	if email not in users:
		return 'User does not exist', 404
	users[email]['status_message'] = status_message
	return 'Status message updated', 200

@app.route('/update_privacy_settings', methods=['POST'])
def update_privacy_settings():
	email = request.json.get('email')
	privacy_settings = request.json.get('privacy_settings')
	if email not in users:
		return 'User does not exist', 404
	users[email]['privacy_settings'] = privacy_settings
	return 'Privacy settings updated', 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	email = request.json.get('email')
	contact = request.json.get('contact')
	if email not in users:
		return 'User does not exist', 404
	if contact not in users[email]['blocked_contacts']:
		users[email]['blocked_contacts'].append(contact)
	return 'Contact blocked', 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	email = request.json.get('email')
	contact = request.json.get('contact')
	if email not in users:
		return 'User does not exist', 404
	if contact in users[email]['blocked_contacts']:
		users[email]['blocked_contacts'].remove(contact)
	return 'Contact unblocked', 200

@app.route('/create_group', methods=['POST'])
def create_group():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	if email not in users:
		return 'User does not exist', 404
	if group_name in users[email]['groups']:
		return 'Group already exists', 400
	users[email]['groups'][group_name] = {'members': [], 'admins': [email]}
	return 'Group created', 201

@app.route('/add_participant', methods=['POST'])
def add_participant():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	participant = request.json.get('participant')
	if email not in users or group_name not in users[email]['groups'] or email not in users[email]['groups'][group_name]['admins']:
		return 'Unauthorized', 401
	if participant in users[email]['groups'][group_name]['members']:
		return 'Participant already in group', 400
	users[email]['groups'][group_name]['members'].append(participant)
	return 'Participant added', 200

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	participant = request.json.get('participant')
	if email not in users or group_name not in users[email]['groups'] or email not in users[email]['groups'][group_name]['admins']:
		return 'Unauthorized', 401
	if participant not in users[email]['groups'][group_name]['members']:
		return 'Participant not in group', 400
	users[email]['groups'][group_name]['members'].remove(participant)
	return 'Participant removed', 200

@app.route('/set_admin', methods=['POST'])
def set_admin():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	admin = request.json.get('admin')
	if email not in users or group_name not in users[email]['groups'] or email not in users[email]['groups'][group_name]['admins']:
		return 'Unauthorized', 401
	if admin in users[email]['groups'][group_name]['admins']:
		return 'User already an admin', 400
	users[email]['groups'][group_name]['admins'].append(admin)
	return 'Admin added', 200

@app.route('/remove_admin', methods=['POST'])
def remove_admin():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	admin = request.json.get('admin')
	if email not in users or group_name not in users[email]['groups'] or email not in users[email]['groups'][group_name]['admins']:
		return 'Unauthorized', 401
	if admin not in users[email]['groups'][group_name]['admins']:
		return 'User not an admin', 400
	users[email]['groups'][group_name]['admins'].remove(admin)
	return 'Admin removed', 200

@app.route('/send_message', methods=['POST'])
def send_message():
	sender = request.json.get('sender')
	receiver = request.json.get('receiver')
	content = request.json.get('content')
	conversation_id = hashlib.sha256((sender + receiver).encode()).hexdigest()
	if conversation_id not in messages:
		messages[conversation_id] = []
	messages[conversation_id].append({'sender': sender, 'receiver': receiver, 'content': content, 'read': False, 'encrypted': False})
	return 'Message sent', 200

@app.route('/read_message', methods=['POST'])
def read_message():
	conversation_id = request.json.get('conversation_id')
	message_index = request.json.get('message_index')
	if conversation_id not in messages or message_index >= len(messages[conversation_id]):
		return 'Message does not exist', 404
	messages[conversation_id][message_index]['read'] = True
	return 'Message marked as read', 200

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message():
	conversation_id = request.json.get('conversation_id')
	message_index = request.json.get('message_index')
	if conversation_id not in messages or message_index >= len(messages[conversation_id]):
		return 'Message does not exist', 404
	messages[conversation_id][message_index]['content'] = hashlib.sha256(messages[conversation_id][message_index]['content'].encode()).hexdigest()
	messages[conversation_id][message_index]['encrypted'] = True
	return 'Message encrypted', 200

@app.route('/decrypt_message', methods=['POST'])
def decrypt_message():
	conversation_id = request.json.get('conversation_id')
	message_index = request.json.get('message_index')
	if conversation_id not in messages or message_index >= len(messages[conversation_id]):
		return 'Message does not exist', 404
	if not messages[conversation_id][message_index]['encrypted']:
		return 'Message is not encrypted', 400
	return 'Decryption not supported', 400

@app.route('/post_status', methods=['POST'])
def post_status():
	email = request.json.get('email')
	image = request.json.get('image')
	visibility = request.json.get('visibility')
	expiry = request.json.get('expiry')
	if email not in users:
		return 'User does not exist', 404
	if email not in statuses:
		statuses[email] = []
	statuses[email].append({'image': image, 'visibility': visibility, 'expiry': expiry, 'timestamp': time.time()})
	return 'Status posted', 200

@app.route('/view_status', methods=['POST'])
def view_status():
	email = request.json.get('email')
	viewer = request.json.get('viewer')
	if email not in users or viewer not in users:
		return 'User does not exist', 404
	if email not in statuses:
		return 'No statuses', 404
	visible_statuses = [status for status in statuses[email] if status['visibility'] == 'public' or viewer in status['visibility']]
	return {'statuses': visible_statuses}, 200

if __name__ == '__main__':
	app.run(debug=True)
