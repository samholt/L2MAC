from flask import Flask, request
from database import users, transactions, accounts, budgets, investments
from models.user import User
from models.transaction import Transaction
from models.account import Account
from models.budget import Budget
from models.investment import Investment

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
	user = User(**request.json)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/transaction', methods=['POST'])
def create_transaction():
	transaction = Transaction(**request.json)
	transactions[transaction.id] = transaction
	return {'id': transaction.id}, 201

@app.route('/account', methods=['POST'])
def create_account():
	account = Account(**request.json)
	accounts[account.id] = account
	return {'id': account.id}, 201

@app.route('/budget', methods=['POST'])
def create_budget():
	budget = Budget(**request.json)
	budgets[budget.id] = budget
	return {'id': budget.id}, 201

@app.route('/investment', methods=['POST'])
def create_investment():
	investment = Investment(**request.json)
	investments[investment.id] = investment
	return {'id': investment.id}, 201
