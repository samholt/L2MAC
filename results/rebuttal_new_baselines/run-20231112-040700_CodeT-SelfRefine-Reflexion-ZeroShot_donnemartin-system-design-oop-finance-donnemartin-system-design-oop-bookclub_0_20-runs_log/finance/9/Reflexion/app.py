from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
transactions = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@dataclass
class Transaction:
	user_email: str
	category: str
	amount: float

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'email' in data and data['email'] in users:
		return jsonify({'message': 'User already exists.'}), 400
	if 'name' not in data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Invalid data.'}), 400
	user = User(data['name'], data['email'], data['password'])
	users[data['email']] = user
	return jsonify({'message': 'User created successfully.'}), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	if 'user_email' not in data or data['user_email'] not in users:
		return jsonify({'message': 'User does not exist.'}), 400
	if 'category' not in data or 'amount' not in data:
		return jsonify({'message': 'Invalid data.'}), 400
	transaction = Transaction(data['user_email'], data['category'], data['amount'])
	transactions[data['user_email']] = transaction
	return jsonify({'message': 'Transaction created successfully.'}), 201

if __name__ == '__main__':
	app.run(debug=True)
