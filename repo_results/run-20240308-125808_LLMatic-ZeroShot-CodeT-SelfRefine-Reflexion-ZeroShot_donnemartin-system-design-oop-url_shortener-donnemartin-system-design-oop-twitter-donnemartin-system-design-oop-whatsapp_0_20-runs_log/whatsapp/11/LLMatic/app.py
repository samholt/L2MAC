from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/app', methods=['GET'])
def app_route():
	return 'Welcome to the App!'

@app.route('/signup', methods=['POST'])
def signup():
	email = request.json.get('email')
	password = request.json.get('password')
	profile_picture = request.json.get('profile_picture')
	status_message = request.json.get('status_message')
	privacy_settings = request.json.get('privacy_settings')
	if email in users:
		return jsonify({'message': 'Email already exists'}), 400
	users[email] = {
		'password': password,
		'profile_picture': profile_picture,
		'status_message': status_message,
		'privacy_settings': privacy_settings,
		'blocked_contacts': [],
		'groups': {},
		'statuses': []
	}
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/update_profile', methods=['POST'])
def update_profile():
	email = request.json.get('email')
	profile_picture = request.json.get('profile_picture')
	status_message = request.json.get('status_message')
	privacy_settings = request.json.get('privacy_settings')
	if email not in users:
		return jsonify({'message': 'Email does not exist'}), 400
	users[email].update({
		'profile_picture': profile_picture,
		'status_message': status_message,
		'privacy_settings': privacy_settings
	})
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post_status', methods=['POST'])
def post_status():
	email = request.json.get('email')
	status = request.json.get('status')
	if email not in users:
		return jsonify({'message': 'Email does not exist'}), 400
	users[email]['statuses'].append(status)
	return jsonify({'message': 'Status posted successfully'}), 200

@app.route('/get_statuses', methods=['GET'])
def get_statuses():
	email = request.args.get('email')
	if email not in users:
		return jsonify({'message': 'Invalid request'}), 400
	return jsonify(users[email]['statuses']), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	email = request.json.get('email')
	contact_email = request.json.get('contact_email')
	if email not in users or contact_email not in users or email == contact_email or contact_email in users[email]['blocked_contacts']:
		return jsonify({'message': 'Invalid request'}), 400
	users[email]['blocked_contacts'].append(contact_email)
	return jsonify({'message': 'Contact blocked successfully'}), 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	email = request.json.get('email')
	contact_email = request.json.get('contact_email')
	if email not in users or contact_email not in users or email == contact_email or contact_email not in users[email]['blocked_contacts']:
		return jsonify({'message': 'Invalid request'}), 400
	users[email]['blocked_contacts'].remove(contact_email)
	return jsonify({'message': 'Contact unblocked successfully'}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	if email not in users or group_name in users[email]['groups']:
		return jsonify({'message': 'Invalid request'}), 400
	users[email]['groups'][group_name] = []
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/edit_group', methods=['POST'])
def edit_group():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	new_group_name = request.json.get('new_group_name')
	if email not in users or group_name not in users[email]['groups'] or new_group_name in users[email]['groups']:
		return jsonify({'message': 'Invalid request'}), 400
	users[email]['groups'][new_group_name] = users[email]['groups'].pop(group_name)
	return jsonify({'message': 'Group edited successfully'}), 200

@app.route('/manage_group', methods=['POST'])
def manage_group():
	email = request.json.get('email')
	group_name = request.json.get('group_name')
	action = request.json.get('action')
	contact_email = request.json.get('contact_email')
	if email not in users or group_name not in users[email]['groups'] or contact_email not in users or (action == 'add' and contact_email in users[email]['groups'][group_name]) or (action == 'remove' and contact_email not in users[email]['groups'][group_name]):
		return jsonify({'message': 'Invalid request'}), 400
	if action == 'add':
		users[email]['groups'][group_name].append(contact_email)
	elif action == 'remove':
		users[email]['groups'][group_name].remove(contact_email)
	return jsonify({'message': 'Group managed successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_email = request.json.get('sender_email')
	recipient_email = request.json.get('recipient_email')
	message = request.json.get('message')
	if sender_email not in users or recipient_email not in users or sender_email == recipient_email:
		return jsonify({'message': 'Invalid request'}), 400
	if sender_email not in messages:
		messages[sender_email] = {}
	messages[sender_email][recipient_email] = message
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/get_messages', methods=['GET'])
def get_messages():
	email = request.args.get('email')
	if email not in users:
		return jsonify({'message': 'Invalid request'}), 400
	user_messages = {}
	for sender, recipients in messages.items():
		if email in recipients:
			user_messages[sender] = recipients[email]
	return jsonify(user_messages), 200

@app.route('/recover', methods=['POST'])
def recover():
	email = request.json.get('email')
	if email not in users:
		return jsonify({'message': 'Email does not exist'}), 400
	return jsonify({'password': users[email]['password']}), 200

if __name__ == '__main__':
	app.run(debug=True)
