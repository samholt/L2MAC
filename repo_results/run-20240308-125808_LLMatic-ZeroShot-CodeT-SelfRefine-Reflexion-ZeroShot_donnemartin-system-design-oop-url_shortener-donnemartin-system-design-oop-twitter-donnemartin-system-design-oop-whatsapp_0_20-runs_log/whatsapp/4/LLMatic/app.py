from flask import Flask, jsonify, request, render_template
import time

app = Flask(__name__)

users = {}
messages = {}
statuses = {}
offline_messages = {}

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
	email = request.json.get('email')
	password = request.json.get('password')
	if email in users:
		return jsonify({'message': 'Email already exists'}), 400
	users[email] = {'password': password, 'profile_picture': None, 'status_message': None, 'privacy_setting': None, 'blocked_contacts': [], 'groups': {}, 'online': True}
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/online_status', methods=['POST'])
def online_status():
	email = request.json.get('email')
	status = request.json.get('status')
	if email not in users:
		return jsonify({'message': 'Email does not exist'}), 404
	users[email]['online'] = status
	return jsonify({'message': 'Online status updated successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_email = request.json.get('sender_email')
	receiver_email = request.json.get('receiver_email')
	message = request.json.get('message')
	if sender_email not in users or receiver_email not in users:
		return jsonify({'message': 'Email does not exist'}), 404
	if users[receiver_email]['online']:
		messages[(sender_email, receiver_email)] = message
		return jsonify({'message': 'Message sent successfully'}), 200
	else:
		if receiver_email not in offline_messages:
			offline_messages[receiver_email] = []
		offline_messages[receiver_email].append((sender_email, message))
		return jsonify({'message': 'Message queued successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
