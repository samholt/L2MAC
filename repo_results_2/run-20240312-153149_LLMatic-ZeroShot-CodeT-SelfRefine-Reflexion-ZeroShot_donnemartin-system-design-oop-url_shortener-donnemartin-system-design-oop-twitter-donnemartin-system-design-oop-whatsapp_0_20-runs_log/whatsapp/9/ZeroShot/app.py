from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'error': 'Missing email or password'}), 400
	if data['email'] in users:
		return jsonify({'error': 'Email already registered'}), 400
	users[data['email']] = {'password': data['password'], 'profile': {}, 'contacts': [], 'groups': [], 'status': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'error': 'Missing email or password'}), 400
	if data['email'] not in users or users[data['email']]['password'] != data['password']:
		return jsonify({'error': 'Invalid email or password'}), 400
	return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	if 'email' not in data or 'profile' not in data:
		return jsonify({'error': 'Missing email or profile data'}), 400
	if data['email'] not in users:
		return jsonify({'error': 'User not found'}), 404
	users[data['email']]['profile'] = data['profile']
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/add_contact', methods=['POST'])
def add_contact():
	data = request.get_json()
	if 'email' not in data or 'contact' not in data:
		return jsonify({'error': 'Missing email or contact'}), 400
	if data['email'] not in users or data['contact'] not in users:
		return jsonify({'error': 'User or contact not found'}), 404
	users[data['email']]['contacts'].append(data['contact'])
	return jsonify({'message': 'Contact added successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if 'sender' not in data or 'receiver' not in data or 'message' not in data:
		return jsonify({'error': 'Missing sender, receiver or message'}), 400
	if data['sender'] not in users or data['receiver'] not in users:
		return jsonify({'error': 'Sender or receiver not found'}), 404
	messages.setdefault(data['sender'], []).append({'to': data['receiver'], 'message': data['message']})
	return jsonify({'message': 'Message sent successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
