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
	username: str
	category: str
	amount: float

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	users[username] = User(username, password)
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	category = data['category']
	amount = data['amount']
	transactions[username] = Transaction(username, category, amount)
	return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/view_transactions', methods=['GET'])
def view_transactions():
	username = request.args.get('username')
	if username in transactions:
		transaction = transactions[username]
		return jsonify({'username': transaction.username, 'category': transaction.category, 'amount': transaction.amount}), 200
	else:
		return jsonify({'message': 'No transactions found for this user'}), 404

if __name__ == '__main__':
	app.run(debug=True)
