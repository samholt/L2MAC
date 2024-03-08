from flask import Flask, request, jsonify
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database
DATABASE = {}
TRANSACTIONS = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	user: str
	category: str
	amount: float

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'], generate_password_hash(data['password']))
	DATABASE[user.username] = user
	TRANSACTIONS[user.username] = []
	return jsonify({'message': 'User created'}), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	user = DATABASE.get(data['user'])
	if user and check_password_hash(user.password, data['password']):
		transaction_data = {key: value for key, value in data.items() if key != 'password'}
		transaction = Transaction(**transaction_data)
		TRANSACTIONS[transaction.user].append(transaction)
		return jsonify({'message': 'Transaction added'}), 201
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
	app.run(debug=True)
