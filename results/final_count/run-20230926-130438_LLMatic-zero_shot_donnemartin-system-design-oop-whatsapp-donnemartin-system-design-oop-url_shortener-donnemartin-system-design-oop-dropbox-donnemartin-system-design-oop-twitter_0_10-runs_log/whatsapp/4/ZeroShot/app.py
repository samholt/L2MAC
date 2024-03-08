from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing email or password'}), 400
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = {'password': data['password']}
	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
