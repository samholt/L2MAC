from flask import Flask, request
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

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = user
	return {'status': 'success'}, 200

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	account = Account(**data)
	DATABASE[account.id] = account
	return {'status': 'success'}, 200

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	DATABASE[transaction.id] = transaction
	return {'status': 'success'}, 200

if __name__ == '__main__':
	app.run(debug=True)
