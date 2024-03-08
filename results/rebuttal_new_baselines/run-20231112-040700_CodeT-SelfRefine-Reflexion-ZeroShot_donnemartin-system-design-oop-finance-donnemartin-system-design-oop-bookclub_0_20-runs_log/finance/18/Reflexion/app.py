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
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.username] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	transactions.setdefault(transaction.user_id, []).append(transaction)
	return jsonify({'message': 'Transaction added'}), 201

@app.route('/get_transactions/<user_id>', methods=['GET'])
def get_transactions(user_id):
	user_transactions = transactions.get(user_id, [])
	return jsonify([t.__dict__ for t in user_transactions]), 200

if __name__ == '__main__':
	app.run(debug=True)
