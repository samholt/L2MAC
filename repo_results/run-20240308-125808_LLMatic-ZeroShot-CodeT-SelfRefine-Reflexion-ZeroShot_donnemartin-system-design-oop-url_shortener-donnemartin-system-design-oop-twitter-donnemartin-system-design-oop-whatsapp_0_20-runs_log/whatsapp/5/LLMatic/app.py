from flask import Flask, request
import hashlib
import time

app = Flask(__name__)

# Mock database
users_db = {}
messages_db = {}
groups_db = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'username' not in data or 'password' not in data:
		return {'message': 'Username and password are required'}, 400
	if data['username'] in users_db:
		return {'message': 'Username already exists'}, 400
	users_db[data['username']] = {'password': hashlib.sha256(data['password'].encode()).hexdigest(), 'contacts': [], 'status': 'offline', 'queue': []}
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'username' not in data or 'password' not in data:
		return {'message': 'Username and password are required'}, 400
	if data['username'] not in users_db or users_db[data['username']]['password'] != hashlib.sha256(data['password'].encode()).hexdigest():
		return {'message': 'Invalid username or password'}, 400
	users_db[data['username']]['status'] = 'online'
	return {'message': 'User logged in successfully'}, 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	if 'username' not in data:
		return {'message': 'Username is required'}, 400
	if data['username'] not in users_db:
		return {'message': 'User does not exist'}, 400
	users_db[data['username']]['status'] = 'offline'
	return {'message': 'User logged out successfully'}, 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	if 'sender' not in data or 'receiver' not in data or 'message' not in data:
		return {'message': 'Sender, receiver and message are required'}, 400
	if data['sender'] not in users_db or data['receiver'] not in users_db:
		return {'message': 'Sender or receiver does not exist'}, 400
	message_id = hashlib.sha256((data['sender'] + data['receiver'] + data['message'] + str(time.time())).encode()).hexdigest()
	message = {'sender': data['sender'], 'receiver': data['receiver'], 'message': data['message'], 'timestamp': time.time()}
	if users_db[data['receiver']]['status'] == 'online':
		messages_db[message_id] = message
		return {'message': 'Message sent successfully', 'message_id': message_id}, 200
	else:
		users_db[data['receiver']]['queue'].append(message)
		return {'message': 'Message queued', 'message_id': message_id}, 200

if __name__ == '__main__':
	app.run(debug=True)
