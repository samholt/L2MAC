from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	id: str
	username: str
	password: str
	bank_accounts: list
	expenses: dict
	incomes: dict
	budgets: dict
	investments: dict

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	user_id = data['user_id']
	bank_account = data['bank_account']
	DATABASE[user_id].bank_accounts.append(bank_account)
	return jsonify({'message': 'Bank account linked successfully'}), 200

@app.route('/add_expense', methods=['POST'])
def add_expense():
	data = request.get_json()
	user_id = data['user_id']
	expense = data['expense']
	DATABASE[user_id].expenses.append(expense)
	return jsonify({'message': 'Expense added successfully'}), 200

@app.route('/add_income', methods=['POST'])
def add_income():
	data = request.get_json()
	user_id = data['user_id']
	income = data['income']
	DATABASE[user_id].incomes.append(income)
	return jsonify({'message': 'Income added successfully'}), 200

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	user_id = data['user_id']
	budget = data['budget']
	DATABASE[user_id].budgets.append(budget)
	return jsonify({'message': 'Budget set successfully'}), 200

@app.route('/add_investment', methods=['POST'])
def add_investment():
	data = request.get_json()
	user_id = data['user_id']
	investment = data['investment']
	DATABASE[user_id].investments.append(investment)
	return jsonify({'message': 'Investment added successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
