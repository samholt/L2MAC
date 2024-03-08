from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}

@dataclass
class User:
	username: str
	password: str
	transactions: list
	budgets: dict
	investments: dict

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, [], {}, {})
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
