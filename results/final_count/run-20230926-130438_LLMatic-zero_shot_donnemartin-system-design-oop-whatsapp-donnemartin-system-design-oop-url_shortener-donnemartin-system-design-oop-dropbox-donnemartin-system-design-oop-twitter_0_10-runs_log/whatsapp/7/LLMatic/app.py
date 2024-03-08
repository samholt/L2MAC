from flask import Flask, request, render_template
import random
import string
from cryptography.fernet import Fernet

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'messages': {},
	'groups': {},
	'statuses': {},
	'profile_pictures': {},
	'privacy_settings': {},
	'blocked_contacts': {},
	'group_details': {},
	'read_receipts': {},
	'encrypted_messages': {},
	'user_status': {},
	'message_queue': {}
}

# Encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def home():
	return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		if email not in DATABASE['users']:
			DATABASE['users'][email] = password
			DATABASE['user_status'][email] = 'offline'
			DATABASE['message_queue'][email] = []
			return render_template('signin.html', message='User created successfully.')
		else:
			return render_template('signup.html', message='User already exists.')
	else:
		return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		if email in DATABASE['users'] and DATABASE['users'][email] == password:
			DATABASE['user_status'][email] = 'online'
			return render_template('profile.html', email=email, profile_picture=DATABASE['profile_pictures'].get(email))
		else:
			return render_template('signin.html', message='Invalid email or password.')
	else:
		return render_template('signin.html')

@app.route('/profile/<email>', methods=['GET'])
def profile(email):
	if email in DATABASE['users']:
		return render_template('profile.html', email=email, profile_picture=DATABASE['profile_pictures'].get(email))
	else:
		return render_template('signin.html', message='User does not exist.')

@app.route('/contacts/<email>', methods=['GET'])
def contacts(email):
	if email in DATABASE['users']:
		return render_template('contacts.html', contacts=DATABASE['blocked_contacts'].get(email, []))
	else:
		return render_template('signin.html', message='User does not exist.')

@app.route('/messages/<email>', methods=['GET'])
def messages(email):
	if email in DATABASE['users']:
		messages = [message for message in DATABASE['messages'].values() if message['sender'] == email or message['receiver'] == email]
		return render_template('messages.html', messages=messages)
	else:
		return render_template('signin.html', message='User does not exist.')

@app.route('/groups/<email>', methods=['GET'])
def groups(email):
	if email in DATABASE['users']:
		groups = [group for group in DATABASE['groups'].values() if email in group['participants']]
		return render_template('groups.html', groups=groups)
	else:
		return render_template('signin.html', message='User does not exist.')

@app.route('/statuses/<email>', methods=['GET'])
def statuses(email):
	if email in DATABASE['users']:
		statuses = [status for status in DATABASE['statuses'].values() if status['user_id'] == email]
		return render_template('statuses.html', statuses=statuses)
	else:
		return render_template('signin.html', message='User does not exist.')

@app.route('/update_status/<email>', methods=['POST'])
def update_status(email):
	status = request.form.get('status')
	if email in DATABASE['users']:
		DATABASE['user_status'][email] = status
		if status == 'online':
			# Send queued messages
			for message in DATABASE['message_queue'][email]:
				DATABASE['messages'][message['id']] = message
			DATABASE['message_queue'][email] = []
		return 'Status updated successfully'
	else:
		return 'User does not exist'

@app.route('/send_message', methods=['POST'])
def send_message():
	email = request.form.get('email')
	receiver = request.form.get('receiver')
	message = request.form.get('message')
	if email in DATABASE['users'] and receiver in DATABASE['users']:
		message_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		message_data = {'id': message_id, 'sender': email, 'receiver': receiver, 'message': message}
		if DATABASE['user_status'][receiver] == 'offline':
			# Queue the message
			DATABASE['message_queue'][receiver].append(message_data)
		else:
			# Send the message
			DATABASE['messages'][message_id] = message_data
		return 'Message sent successfully'
	else:
		return 'User does not exist'

if __name__ == '__main__':
	app.run(debug=True)
