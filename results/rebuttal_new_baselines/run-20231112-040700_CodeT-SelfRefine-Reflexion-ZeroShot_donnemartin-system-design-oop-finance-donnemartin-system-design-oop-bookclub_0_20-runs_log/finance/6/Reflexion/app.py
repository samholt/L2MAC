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

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	user = data['user']
	amount = data['amount']
	category = data['category']
	transactions[user] = Transaction(user, amount, category)
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
