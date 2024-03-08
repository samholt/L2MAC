from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

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
class BankAccount:
	id: str
	user_id: str
	balance: float

@dataclass
class Budget:
	id: str
	user_id: str
	category: str
	limit: float

@dataclass
class Investment:
	id: str
	user_id: str
	value: float
	roi: float

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = user
	return jsonify(user), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	DATABASE[transaction.id] = transaction
	return jsonify(transaction), 201

@app.route('/create_bank_account', methods=['POST'])
def create_bank_account():
	data = request.get_json()
	bank_account = BankAccount(**data)
	DATABASE[bank_account.id] = bank_account
	return jsonify(bank_account), 201

@app.route('/create_budget', methods=['POST'])
def create_budget():
	data = request.get_json()
	budget = Budget(**data)
	DATABASE[budget.id] = budget
	return jsonify(budget), 201

@app.route('/create_investment', methods=['POST'])
def create_investment():
	data = request.get_json()
	investment = Investment(**data)
	DATABASE[investment.id] = investment
	return jsonify(investment), 201

if __name__ == '__main__':
	app.run(debug=True)
