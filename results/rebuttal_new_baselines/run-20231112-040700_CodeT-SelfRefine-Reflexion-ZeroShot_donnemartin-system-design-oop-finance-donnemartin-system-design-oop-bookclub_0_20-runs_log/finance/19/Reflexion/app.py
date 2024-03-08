from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
transactions = {}

@dataclass
class User:
	id: str
	email: str
	password: str

@dataclass
class Transaction:
	id: str
	user_id: str
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'message': 'User created successfully'}, 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	transactions[transaction.id] = transaction
	return {'message': 'Transaction added successfully'}, 201

@app.route('/get_transactions/<user_id>', methods=['GET'])
def get_transactions(user_id):
	user_transactions = [t for t in transactions.values() if t.user_id == user_id]
	return {'transactions': [t.__dict__ for t in user_transactions]}, 200

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	if user_id in users:
		del users[user_id]
		return {'message': 'User deleted successfully'}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/delete_transaction/<transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
	if transaction_id in transactions:
		del transactions[transaction_id]
		return {'message': 'Transaction deleted successfully'}, 200
	else:
		return {'message': 'Transaction not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
