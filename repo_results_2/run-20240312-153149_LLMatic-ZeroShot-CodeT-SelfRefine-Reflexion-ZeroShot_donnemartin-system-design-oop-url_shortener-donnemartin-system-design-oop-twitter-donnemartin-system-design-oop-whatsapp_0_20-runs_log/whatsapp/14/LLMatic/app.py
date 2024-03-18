from flask import Flask, request
import hashlib

app = Flask(__name__)

# Mock database
users_db = {}
groups_db = {}
messages_queue = {}

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = data
	users_db[data['email']]['online'] = 'offline'
	messages_queue[data['email']] = []
	return {'message': 'User created'}, 201

@app.route('/users/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/online_status', methods=['POST'])
def update_online_status():
	data = request.get_json()
	if 'email' not in data or 'status' not in data:
		return {'message': 'Email and status are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'Email does not exist'}, 404
	users_db[data['email']]['online'] = data['status']
	if data['status'] == 'online':
		# Send queued messages
		queued_messages = messages_queue.get(data['email'], [])
		messages_queue[data['email']] = []
		return {'message': 'User is online', 'queued_messages': queued_messages}, 200
	return {'message': 'User is offline'}, 200

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	if 'email' not in data or 'status' not in data or 'visibility' not in data:
		return {'message': 'Email, status and visibility are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'Email does not exist'}, 404
	users_db[data['email']]['status'] = data['status']
	users_db[data['email']]['visibility'] = data['visibility']
	return {'message': 'Status posted successfully'}, 200

@app.route('/manage_visibility', methods=['POST'])
def manage_visibility():
	data = request.get_json()
	if 'email' not in data or 'visibility' not in data:
		return {'message': 'Email and visibility are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'Email does not exist'}, 404
	users_db[data['email']]['visibility'] = data['visibility']
	return {'message': 'Visibility updated successfully'}, 200

# Existing routes...

