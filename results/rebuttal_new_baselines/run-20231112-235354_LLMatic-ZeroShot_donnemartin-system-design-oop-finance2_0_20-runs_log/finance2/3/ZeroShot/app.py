from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
DB = {}

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
	DB[user.id] = user
	return {'status': 'success'}, 200

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	user_id = data['user_id']
	bank_account = data['bank_account']
	DB[user_id].bank_accounts.append(bank_account)
	return {'status': 'success'}, 200

@app.route('/add_expense', methods=['POST'])
def add_expense():
	data = request.get_json()
	user_id = data['user_id']
	expense = data['expense']
	DB[user_id].expenses.append(expense)
	return {'status': 'success'}, 200

@app.route('/add_income', methods=['POST'])
def add_income():
	data = request.get_json()
	user_id = data['user_id']
	income = data['income']
	DB[user_id].incomes.append(income)
	return {'status': 'success'}, 200

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	user_id = data['user_id']
	budget = data['budget']
	DB[user_id].budgets = budget
	return {'status': 'success'}, 200

@app.route('/add_investment', methods=['POST'])
def add_investment():
	data = request.get_json()
	user_id = data['user_id']
	investment = data['investment']
	DB[user_id].investments.append(investment)
	return {'status': 'success'}, 200

if __name__ == '__main__':
	app.run(debug=True)
