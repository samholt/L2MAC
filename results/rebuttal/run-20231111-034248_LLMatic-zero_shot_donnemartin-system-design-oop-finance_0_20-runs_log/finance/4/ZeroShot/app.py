from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
transactions = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	user_id: str
	type: str
	amount: float
	category: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data.get('username'))
	if user and user.password == data.get('password'):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	transactions.setdefault(transaction.user_id, []).append(transaction)
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
