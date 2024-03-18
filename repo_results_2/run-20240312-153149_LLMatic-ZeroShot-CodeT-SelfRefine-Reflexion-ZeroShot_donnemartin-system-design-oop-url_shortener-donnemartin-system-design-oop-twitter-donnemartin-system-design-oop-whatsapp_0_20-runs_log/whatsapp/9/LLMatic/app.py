from flask import Flask, request
import time

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
	return 'Welcome to the User Management System!', 200

@app.route('/signup', methods=['POST'])
def signup():
	email = request.form.get('email')
	password = request.form.get('password')
	if email not in users:
		users[email] = {'password': password, 'profile_picture': None, 'status_message': None, 'privacy_settings': 'public', 'blocked': [], 'groups': {}, 'messages': [], 'status': None}
		return 'User created successfully', 201
	else:
		return 'User already exists', 400

@app.route('/recover', methods=['GET'])
def recover():
	email = request.args.get('email')
	if email in users:
		return users[email]['password'], 200
	else:
		return 'User not found', 404

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	email = request.form.get('email')
	profile_picture = request.form.get('profile_picture')
	if email in users:
		users[email]['profile_picture'] = profile_picture
		return 'Profile picture updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	email = request.form.get('email')
	status_message = request.form.get('status_message')
	if email in users:
		users[email]['status_message'] = status_message
		return 'Status message updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/set_privacy_settings', methods=['POST'])
def set_privacy_settings():
	email = request.form.get('email')
	privacy_settings = request.form.get('privacy_settings')
	if email in users:
		users[email]['privacy_settings'] = privacy_settings
		return 'Privacy settings updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/block', methods=['POST'])
def block():
	email = request.form.get('email')
	block_email = request.form.get('block_email')
	if email in users and block_email not in users[email]['blocked']:
		users[email]['blocked'].append(block_email)
		return 'User blocked successfully', 200
	else:
		return 'User not found or already blocked', 404

@app.route('/unblock', methods=['POST'])
def unblock():
	email = request.form.get('email')
	unblock_email = request.form.get('unblock_email')
	if email in users and unblock_email in users[email]['blocked']:
		users[email]['blocked'].remove(unblock_email)
		return 'User unblocked successfully', 200
	else:
		return 'User not found or not blocked', 404

@app.route('/create_group', methods=['POST'])
def create_group():
	email = request.form.get('email')
	group_name = request.form.get('group_name')
	if email in users and group_name not in users[email]['groups']:
		users[email]['groups'][group_name] = []
		return 'Group created successfully', 200
	else:
		return 'User not found or group already exists', 404

@app.route('/edit_group', methods=['POST'])
def edit_group():
	email = request.form.get('email')
	group_name = request.form.get('group_name')
	new_group_name = request.form.get('new_group_name')
	if email in users and group_name in users[email]['groups']:
		users[email]['groups'][new_group_name] = users[email]['groups'].pop(group_name)
		return 'Group edited successfully', 200
	else:
		return 'User not found or group does not exist', 404

@app.route('/manage_group', methods=['POST'])
def manage_group():
	email = request.form.get('email')
	group_name = request.form.get('group_name')
	action = request.form.get('action')
	member_email = request.form.get('member_email')
	if email in users and group_name in users[email]['groups']:
		if action == 'add' and member_email not in users[email]['groups'][group_name]:
			users[email]['groups'][group_name].append(member_email)
			return 'Member added to group successfully', 200
		elif action == 'remove' and member_email in users[email]['groups'][group_name]:
			users[email]['groups'][group_name].remove(member_email)
			return 'Member removed from group successfully', 200
		else:
			return 'Invalid action or member not found', 404
	else:
		return 'User not found or group does not exist', 404

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_email = request.form.get('sender_email')
	receiver_email = request.form.get('receiver_email')
	message = request.form.get('message')
	if sender_email in users and receiver_email in users and receiver_email not in users[sender_email]['blocked']:
		users[sender_email]['messages'].append({'to': receiver_email, 'message': message, 'read': False})
		users[receiver_email]['messages'].append({'from': sender_email, 'message': message, 'read': False})
		return 'Message sent successfully', 200
	else:
		return 'User not found or blocked', 404

@app.route('/read_message', methods=['POST'])
def read_message():
	email = request.form.get('email')
	message_index = int(request.form.get('message_index'))
	if email in users and message_index < len(users[email]['messages']):
		users[email]['messages'][message_index]['read'] = True
		return 'Message marked as read', 200
	else:
		return 'User not found or invalid message index', 404

@app.route('/post_status', methods=['POST'])
def post_status():
	email = request.form.get('email')
	status_image = request.form.get('status_image')
	if email in users:
		users[email]['status'] = {'image': status_image, 'timestamp': time.time()}
		return 'Status posted successfully', 200
	else:
		return 'User not found', 404

@app.route('/view_status', methods=['GET'])
def view_status():
	email = request.args.get('email')
	viewer_email = request.args.get('viewer_email')
	if email in users and viewer_email in users and email not in users[viewer_email]['blocked'] and (users[email]['privacy_settings'] == 'public' or viewer_email in users[email]['groups']):
		status = users[email]['status']
		if status and time.time() - status['timestamp'] <= 24 * 60 * 60:
			return status['image'], 200
		else:
			return 'No status found', 404
	else:
		return 'User not found, blocked, or private', 404
