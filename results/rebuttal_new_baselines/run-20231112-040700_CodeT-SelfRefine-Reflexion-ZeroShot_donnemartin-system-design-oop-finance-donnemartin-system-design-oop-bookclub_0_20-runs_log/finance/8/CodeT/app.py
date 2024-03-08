from flask import Flask, request, jsonify
from dataclasses import dataclass
import hashlib

app = Flask(__name__)

# Mock database
users_db = {}
transactions_db = {}

@dataclass
class User:
	username: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username in users_db:
		return jsonify({'message': 'User already exists'}), 400
	users_db[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username not in users_db or users_db[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
