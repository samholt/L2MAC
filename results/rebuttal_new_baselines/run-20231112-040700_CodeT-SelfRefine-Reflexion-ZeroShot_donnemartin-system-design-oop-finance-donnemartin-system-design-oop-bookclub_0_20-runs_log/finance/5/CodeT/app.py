from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users_db = {}
transactions_db = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	user: str
	type: str
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users_db[user.username] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users_db.get(username)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	transactions_db[transaction.user] = transactions_db.get(transaction.user, []) + [transaction]
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
