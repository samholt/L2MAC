from flask import Flask, request, jsonify
import base64
import time

app = Flask(__name__)

users = {}
messages = {}
groups = {}
statuses = {}
offline_messages = {}

@app.route('/')
def home():
	return 'Welcome to the Chat Application!'

@app.route('/register', methods=['POST'])
def register():
	user_id = request.json['user_id']
	if user_id not in users:
		users[user_id] = {'groups': [], 'statuses': [], 'online': True}
		messages[user_id] = {}
		offline_messages[user_id] = []
		return jsonify({'message': 'User registered successfully.'}), 201
	else:
		return jsonify({'message': 'User already exists.'}), 400

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_id = request.json['sender_id']
	receiver_id = request.json['receiver_id']
	message = request.json['message']
	if sender_id in users and receiver_id in users:
		if users[receiver_id]['online']:
			if receiver_id not in messages[sender_id]:
				messages[sender_id][receiver_id] = []
			messages[sender_id][receiver_id].append({'message': message, 'read': False})
			return jsonify({'message': 'Message sent successfully.'}), 200
		else:
			offline_messages[receiver_id].append({'sender_id': sender_id, 'message': message})
			return jsonify({'message': 'User is offline. Message queued.'}), 200
	else:
		return jsonify({'message': 'User does not exist.'}), 400

@app.route('/receive_message', methods=['GET'])
def receive_message():
	sender_id = request.args.get('sender_id')
	receiver_id = request.args.get('receiver_id')
	if sender_id in messages and receiver_id in messages[sender_id]:
		for message in messages[sender_id][receiver_id]:
			message['read'] = True
		return jsonify(messages[sender_id][receiver_id])
	else:
		return jsonify({'message': 'No messages found.'}), 404

@app.route('/set_online_status', methods=['POST'])
def set_online_status():
	user_id = request.json['user_id']
	online_status = request.json['online_status']
	if user_id in users:
		users[user_id]['online'] = online_status
		if online_status and user_id in offline_messages:
			for message in offline_messages[user_id]:
				if user_id not in messages[message['sender_id']]:
					messages[message['sender_id']][user_id] = []
				messages[message['sender_id']][user_id].append({'message': message['message'], 'read': False})
			offline_messages[user_id] = []
		return jsonify({'message': 'Online status set successfully.'}), 200
	else:
		return jsonify({'message': 'User does not exist.'}), 400

@app.route('/get_online_status', methods=['GET'])
def get_online_status():
	user_id = request.args.get('user_id')
	if user_id in users:
		return jsonify({'online_status': users[user_id]['online']}), 200
	else:
		return jsonify({'message': 'User does not exist.'}), 400

# Existing code...

if __name__ == '__main__':
	app.run(debug=True)
