from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
transactions = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	user: str
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	users[username] = User(username, password)
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users and users[username].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	amount = data['amount']
	category = data['category']
	if username in users:
		transaction = Transaction(username, amount, category)
		transactions[username] = transactions.get(username, []) + [transaction]
		return jsonify({'message': 'Transaction added successfully'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
