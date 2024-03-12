from flask import Flask, request
import hashlib

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'messages': {},
	'groups': {},
	'statuses': {},
	'offline_messages': {}
}

@app.route('/')
def home():
	return 'Welcome to the Chat App!'

@app.route('/signup', methods=['POST'])
def signup():
	email = request.json.get('email')
	password = request.json.get('password')
	if email not in DATABASE['users']:
		DATABASE['users'][email] = {'password': password, 'blocked_contacts': [], 'online': False}
		return {'message': 'User registered successfully'}, 201
	else:
		return {'message': 'User already exists'}, 400

@app.route('/login', methods=['POST'])
def login():
	email = request.json.get('email')
	password = request.json.get('password')
	if email in DATABASE['users'] and DATABASE['users'][email]['password'] == password:
		DATABASE['users'][email]['online'] = True
		# Send queued messages
		for message_id, message in list(DATABASE['offline_messages'].items()):
			if message['receiver'] == email:
				DATABASE['messages'][message_id] = message
				del DATABASE['offline_messages'][message_id]
		return {'message': 'User logged in successfully'}, 200
	else:
		return {'message': 'Invalid email or password'}, 400

@app.route('/logout', methods=['POST'])
def logout():
	email = request.json.get('email')
	if email in DATABASE['users']:
		DATABASE['users'][email]['online'] = False
		return {'message': 'User logged out successfully'}, 200
	else:
		return {'message': 'User does not exist'}, 404

@app.route('/send_message', methods=['POST'])
def send_message():
	sender = request.json.get('sender')
	receiver = request.json.get('receiver')
	message = request.json.get('message')
	image_url = request.json.get('image_url')
	if sender in DATABASE['users'] and receiver in DATABASE['users']:
		message_id = hashlib.md5((sender + receiver + message).encode()).hexdigest()
		if DATABASE['users'][receiver]['online']:
			DATABASE['messages'][message_id] = {'sender': sender, 'receiver': receiver, 'message': message, 'read': False, 'image_url': image_url}
			return {'message': 'Message sent successfully', 'message_id': message_id}, 200
		else:
			DATABASE['offline_messages'][message_id] = {'sender': sender, 'receiver': receiver, 'message': message, 'read': False, 'image_url': image_url}
			return {'message': 'Message queued successfully', 'message_id': message_id}, 200
	else:
		return {'message': 'Sender or receiver does not exist'}, 400

@app.route('/receive_message', methods=['POST'])
def receive_message():
	message_id = request.json.get('message_id')
	if message_id in DATABASE['messages']:
		return {'message': DATABASE['messages'][message_id]['message'], 'image_url': DATABASE['messages'][message_id]['image_url']}, 200
	else:
		return {'message': 'Message does not exist'}, 404

@app.route('/read_receipt', methods=['POST'])
def read_receipt():
	message_id = request.json.get('message_id')
	if message_id in DATABASE['messages']:
		DATABASE['messages'][message_id]['read'] = True
		return {'message': 'Read receipt sent'}, 200
	else:
		return {'message': 'Message does not exist'}, 404

# Rest of the code remains the same

if __name__ == '__main__':
	app.run(debug=True)
