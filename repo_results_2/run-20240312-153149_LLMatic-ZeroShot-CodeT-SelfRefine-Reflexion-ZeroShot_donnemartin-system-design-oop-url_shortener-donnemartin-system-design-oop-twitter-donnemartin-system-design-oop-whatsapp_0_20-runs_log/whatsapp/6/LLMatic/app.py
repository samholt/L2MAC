from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'messages': {},
	'groups': {},
	'statuses': {},
	'profiles': {},
	'blocked': {}
}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing parameters'}), 400
	DATABASE['users'][data['email']] = {
		'password': data['password'],
		'profile_picture': '',
		'status_message': '',
		'privacy_settings': '',
		'blocked': [],
		'online': False
	}
	return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing parameters'}), 401
	if data['email'] in DATABASE['users'] and DATABASE['users'][data['email']]['password'] == data['password']:
		DATABASE['users'][data['email']]['online'] = True
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	if 'email' not in data:
		return jsonify({'message': 'Missing parameters'}), 400
	if data['email'] in DATABASE['users']:
		DATABASE['users'][data['email']]['online'] = False
		return jsonify({'message': 'Logout successful'}), 200
	return jsonify({'message': 'Email not found'}), 404

@app.route('/set_status', methods=['POST'])
def set_status():
	data = request.get_json()
	if 'email' not in data or 'status' not in data:
		return jsonify({'message': 'Missing parameters'}), 400
	if data['email'] in DATABASE['users']:
		DATABASE['users'][data['email']]['online'] = data['status']
		return jsonify({'message': 'Status updated'}), 200
	return jsonify({'message': 'Email not found'}), 404

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if 'sender' not in data or 'receiver' not in data or 'message' not in data:
		return jsonify({'message': 'Missing parameters'}), 400
	if data['sender'] in DATABASE['users'] and data['receiver'] in DATABASE['users']:
		message_status = 'sent' if DATABASE['users'][data['receiver']]['online'] else 'queued'
		DATABASE['messages'][data['sender'] + '-' + data['receiver']] = {
			'message': data['message'],
			'status': message_status
		}
		return jsonify({'message': 'Message sent', 'status': message_status}), 200
	return jsonify({'message': 'Invalid sender or receiver'}), 404

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if 'email' not in data:
		return jsonify({'message': 'Missing parameters'}), 400
	if data['email'] in DATABASE['users']:
		return jsonify({'message': 'Password reset link sent'}), 200
	return jsonify({'message': 'Email not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
