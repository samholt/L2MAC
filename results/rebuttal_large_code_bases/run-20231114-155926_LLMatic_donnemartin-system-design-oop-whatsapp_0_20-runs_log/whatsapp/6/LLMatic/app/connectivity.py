from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta

connectivity = Blueprint('connectivity', __name__)

# Mocking a database with an in-memory dictionary
offline_messages = {}
last_activity = {}

@connectivity.route('/status', methods=['GET'])
def check_status():
	# This function checks if the server is online or offline
	# For the purpose of this task, we will always return online
	return jsonify({'status': 'online'}), 200

@connectivity.route('/online_status', methods=['GET'])
def online_status():
	# This function checks the user's online status based on their last activity timestamp
	user_id = request.args.get('user_id')
	if not user_id or user_id not in last_activity:
		return jsonify({'error': 'Invalid user id'}), 400
	# If the user's last activity was less than 5 minutes ago, consider them online
	if datetime.now() - last_activity[user_id] < timedelta(minutes=5):
		return jsonify({'online_status': 'online'}), 200
	else:
		return jsonify({'online_status': 'offline'}), 200

@connectivity.route('/queue', methods=['POST'])
def queue_message():
	# This function queues messages when the server is offline
	# For the purpose of this task, we will just store the messages in the in-memory dictionary
	message = request.get_json()
	if not message or 'user_id' not in message or 'content' not in message:
		return jsonify({'error': 'Invalid request'}), 400
	user_id = message['user_id']
	content = message['content']
	if user_id not in offline_messages:
		offline_messages[user_id] = []
	offline_messages[user_id].append(content)
	# Update the user's last activity timestamp
	last_activity[user_id] = datetime.now()
	return jsonify({'message': 'Message queued'}), 200
