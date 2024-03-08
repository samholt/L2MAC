from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

users = {}
accounts = {}
transactions = {}

@dataclass
class User:
	id: str
	email: str
	password: str

@dataclass
class Account:
	id: str
	user_id: str
	balance: float

@dataclass
class Transaction:
	id: str
	account_id: str
	amount: float
	category: str

@app.route('/users', methods=['POST'])
def create_user():
	user = User(**request.json)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/users/<user_id>/accounts', methods=['POST'])
def create_account(user_id):
	account = Account(user_id=user_id, **request.json)
	accounts[account.id] = account
	return {'id': account.id}, 201

@app.route('/users/<user_id>/accounts', methods=['GET'])
def get_accounts(user_id):
	return {'accounts': [a for a in accounts.values() if a.user_id == user_id]}

@app.route('/accounts/<account_id>/transactions', methods=['POST'])
def create_transaction(account_id):
	transaction = Transaction(account_id=account_id, **request.json)
	transactions[transaction.id] = transaction
	return {'id': transaction.id}, 201

@app.route('/accounts/<account_id>/transactions', methods=['GET'])
def get_transactions(account_id):
	return {'transactions': [t for t in transactions.values() if t.account_id == account_id]}

if __name__ == '__main__':
	app.run(debug=True)
