from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

users = {}
transactions = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	username: str
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
	if users.get(username) and users[username].password == password:
		return jsonify({'message': 'Logged in successfully'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	amount = data['amount']
	category = data['category']
	if users.get(username):
		transaction = Transaction(username, amount, category)
		transactions[username] = transactions.get(username, []) + [transaction]
		return jsonify({'message': 'Transaction added successfully'}), 201
	else:
		return jsonify({'message': 'User does not exist'}), 404

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
	username = request.args.get('username')
	if users.get(username):
		user_transactions = transactions.get(username, [])
		return jsonify([transaction.__dict__ for transaction in user_transactions]), 200
	else:
		return jsonify({'message': 'User does not exist'}), 404

if __name__ == '__main__':
	app.run(debug=True)
