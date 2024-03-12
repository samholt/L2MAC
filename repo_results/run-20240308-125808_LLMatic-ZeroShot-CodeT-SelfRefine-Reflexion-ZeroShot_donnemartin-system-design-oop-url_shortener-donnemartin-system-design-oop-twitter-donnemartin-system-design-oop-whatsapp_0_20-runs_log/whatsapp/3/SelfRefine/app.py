from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
messages = {}
groups = {}
statuses = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = {'password': data['password'], 'profile': {}, 'contacts': [], 'blocked': []}
	return jsonify({'message': 'Registration successful'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']]['password'] != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Login successful'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	users[data['email']]['password'] = data['new_password']
	return jsonify({'message': 'Password reset successful'}), 200

@app.route('/set_profile', methods=['POST'])
def set_profile():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	users[data['email']]['profile'] = data['profile']
	return jsonify({'message': 'Profile set successful'}), 200

@app.route('/add_contact', methods=['POST'])
def add_contact():
	data = request.get_json()
	if data['email'] not in users or data['contact'] not in users:
		return jsonify({'message': 'Email or contact not registered'}), 400
	users[data['email']]['contacts'].append(data['contact'])
	return jsonify({'message': 'Contact added'}), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	if data['contact'] not in users[data['email']]['contacts']:
		return jsonify({'message': 'Contact not found'}), 400
	users[data['email']]['blocked'].append(data['contact'])
	return jsonify({'message': 'Contact blocked'}), 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	if data['contact'] not in users[data['email']]['blocked']:
		return jsonify({'message': 'Contact not blocked'}), 400
	users[data['email']]['blocked'].remove(data['contact'])
	return jsonify({'message': 'Contact unblocked'}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	group_id = len(groups) + 1
	groups[group_id] = {'name': data['name'], 'picture': data['picture'], 'members': [data['email']], 'admins': [data['email']]}
	return jsonify({'message': 'Group created', 'group_id': group_id}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message_id = len(messages) + 1
	messages[message_id] = {'sender': data['email'], 'receiver': data['receiver'], 'message': data['message'], 'read': False}
	return jsonify({'message': 'Message sent', 'message_id': message_id}), 200

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	if data['message_id'] not in messages:
		return jsonify({'message': 'Message not found'}), 400
	messages[data['message_id']]['read'] = True
	return jsonify({'message': 'Message marked as read'}), 200

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	status_id = len(statuses) + 1
	statuses[status_id] = {'user': data['email'], 'status': data['status'], 'visibility': data['visibility']}
	return jsonify({'message': 'Status posted', 'status_id': status_id}), 200

if __name__ == '__main__':
	app.run(debug=True)
