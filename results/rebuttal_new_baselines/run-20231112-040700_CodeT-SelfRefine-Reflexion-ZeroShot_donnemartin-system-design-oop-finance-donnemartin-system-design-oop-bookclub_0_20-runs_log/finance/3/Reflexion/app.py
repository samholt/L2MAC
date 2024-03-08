from flask import Flask, request, jsonify
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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return jsonify(user), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/transactions', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	transactions[transaction.id] = transaction
	return jsonify(transaction), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
	user_id = request.args.get('user_id')
	user_transactions = [t for t in transactions.values() if t.user_id == user_id]
	return jsonify(user_transactions), 200

if __name__ == '__main__':
	app.run(debug=True)
