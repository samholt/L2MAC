from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
messages = []

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = {'password': data['password'], 'profile': {}, 'contacts': [], 'groups': [], 'status': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']]['password'] != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	users[data['email']]['password'] = data['new_password']
	return jsonify({'message': 'Password updated successfully'}), 200

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	users[data['email']]['profile'] = data['profile']
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	if data['contact'] not in users[data['email']]['contacts']:
		return jsonify({'message': 'Contact not found'}), 400
	users[data['email']]['contacts'].remove(data['contact'])
	return jsonify({'message': 'Contact blocked successfully'}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'Email not registered'}), 400
	group = {'name': data['name'], 'members': [data['email']]} # The creator is the first member
	users[data['email']]['groups'].append(group)
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if data['sender'] not in users:
		return jsonify({'message': 'Sender not registered'}), 400
	if data['receiver'] not in users:
		return jsonify({'message': 'Receiver not registered'}), 400
	message = {'sender': data['sender'], 'receiver': data['receiver'], 'content': data['content']}
	messages.append(message)
	return jsonify({'message': 'Message sent successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
