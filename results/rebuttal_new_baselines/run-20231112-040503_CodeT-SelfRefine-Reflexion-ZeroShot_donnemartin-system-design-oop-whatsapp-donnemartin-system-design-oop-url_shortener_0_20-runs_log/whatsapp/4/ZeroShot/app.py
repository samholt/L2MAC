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
	users[data['email']] = {'password': data['password']}
	return jsonify({'success': 'User registered'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'error': 'Missing email or password'}), 400
	if data['email'] not in users or users[data['email']]['password'] != data['password']:
		return jsonify({'error': 'Invalid email or password'}), 400
	return jsonify({'success': 'User logged in'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if 'sender' not in data or 'receiver' not in data or 'message' not in data:
		return jsonify({'error': 'Missing sender, receiver or message'}), 400
	if data['sender'] not in users or data['receiver'] not in users:
		return jsonify({'error': 'Invalid sender or receiver'}), 400
	messages.setdefault(data['sender'], []).append({'to': data['receiver'], 'message': data['message']})
	return jsonify({'success': 'Message sent'}), 200

@app.route('/get_messages', methods=['GET'])
def get_messages():
	user = request.args.get('user')
	if user not in users:
		return jsonify({'error': 'Invalid user'}), 400
	return jsonify({'messages': messages.get(user, [])}), 200

if __name__ == '__main__':
	app.run(debug=True)
