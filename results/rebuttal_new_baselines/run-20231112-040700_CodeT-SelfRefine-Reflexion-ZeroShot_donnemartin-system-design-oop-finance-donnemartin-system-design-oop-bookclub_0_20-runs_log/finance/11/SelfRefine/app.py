from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database
users_db = {}
transactions_db = {}

@dataclass
class User:
	id: str
	username: str
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
	data['password'] = generate_password_hash(data['password'])
	user = User(**data)
	users_db[user.id] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	if data['user_id'] not in users_db or not check_password_hash(users_db[data['user_id']].password, data['password']):
		return jsonify({'message': 'Unauthorized'}), 401
	del data['password']
	transaction = Transaction(**data)
	transactions_db[transaction.id] = transaction
	return jsonify({'message': 'Transaction created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
