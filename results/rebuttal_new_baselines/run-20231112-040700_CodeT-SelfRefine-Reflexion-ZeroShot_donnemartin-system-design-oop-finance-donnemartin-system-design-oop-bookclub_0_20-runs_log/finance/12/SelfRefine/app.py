from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

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
	user = User(**data)
	if user.username in DATABASE:
		return jsonify({'message': 'User already exists'}), 400
	DATABASE[user.username] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	if transaction.user not in DATABASE:
		return jsonify({'message': 'User not found'}), 404
	if 'transactions' not in DATABASE[transaction.user].__dict__:
		DATABASE[transaction.user].__dict__['transactions'] = []
	DATABASE[transaction.user].__dict__['transactions'].append(transaction)
	return jsonify({'message': 'Transaction added'}), 201

if __name__ == '__main__':
	app.run(debug=True)
