from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
transactions = {}

@dataclass
class User:
	username: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/transactions', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	transaction = data['transaction']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 404
	if username not in transactions:
		transactions[username] = []
	transactions[username].append(transaction)
	return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
	username = request.args.get('username')
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 404
	if username not in transactions:
		return jsonify({'transactions': []}), 200
	return jsonify({'transactions': transactions[username]}), 200

if __name__ == '__main__':
	app.run(debug=True)
