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

@dataclass
class Transaction:
	user: str
	category: str
	amount: float

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	users_db[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if users_db.get(username) and users_db[username].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	category = data['category']
	amount = data['amount']
	if users_db.get(username):
		transaction = Transaction(username, category, amount)
		transactions_db[username] = transactions_db.get(username, []) + [transaction]
		return jsonify({'message': 'Transaction added successfully'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/transactions', methods=['GET'])
def get_transactions():
	username = request.args.get('username')
	if users_db.get(username):
		user_transactions = transactions_db.get(username, [])
		return jsonify([transaction.__dict__ for transaction in user_transactions]), 200
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
