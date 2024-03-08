from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
transactions = {}
budgets = {}
investments = {}

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
	recurring: bool

@dataclass
class Budget:
	id: str
	user_id: str
	category: str
	amount: float

@dataclass
class Investment:
	id: str
	user_id: str
	value: float
	roi: float

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(id=data['id'], username=data['username'], password=data['password'])
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/transactions', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(id=data['id'], user_id=data['user_id'], amount=data['amount'], category=data['category'], recurring=data['recurring'])
	transactions[transaction.id] = transaction
	return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/budgets', methods=['POST'])
def add_budget():
	data = request.get_json()
	budget = Budget(id=data['id'], user_id=data['user_id'], category=data['category'], amount=data['amount'])
	budgets[budget.id] = budget
	return jsonify({'message': 'Budget added successfully'}), 201

@app.route('/investments', methods=['POST'])
def add_investment():
	data = request.get_json()
	investment = Investment(id=data['id'], user_id=data['user_id'], value=data['value'], roi=data['roi'])
	investments[investment.id] = investment
	return jsonify({'message': 'Investment added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
