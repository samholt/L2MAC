from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users_db = {}

@dataclass
class User:
	username: str
	password: str

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users_db:
		return jsonify({'message': 'Username already exists'}), 400
	user = User(username, password)
	users_db[username] = user
	return jsonify({'message': 'Account created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
