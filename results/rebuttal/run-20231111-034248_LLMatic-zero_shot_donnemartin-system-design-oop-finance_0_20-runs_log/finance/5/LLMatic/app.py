from flask import Flask, request, jsonify
from user import User
from transaction import Transaction
from account import Account
from investment import Investment

app = Flask(__name__)

users = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	email = data['email']
	users[username] = User(username, password, email)
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if user:
		return jsonify({'username': user.username, 'email': user.email}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/user/<username>/transaction', methods=['POST'])
def create_transaction(username):
	user = users.get(username)
	if user:
		data = request.get_json()
		amount = data['amount']
		category = data['category']
		date = data['date']
		is_recurring = data['is_recurring']
		is_deposit = data['is_deposit']
		transaction = Transaction(amount, category, date, is_recurring, is_deposit)
		user.accounts[0].transactions.append(transaction)
		return jsonify({'message': 'Transaction created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/user/<username>/account', methods=['POST'])
def create_account(username):
	user = users.get(username)
	if user:
		data = request.get_json()
		account_number = data['account_number']
		bank_name = data['bank_name']
		account = Account(account_number, bank_name)
		user.accounts.append(account)
		return jsonify({'message': 'Account created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/user/<username>/investment', methods=['POST'])
def create_investment(username):
	user = users.get(username)
	if user:
		data = request.get_json()
		investment_name = data['investment_name']
		investment_type = data['investment_type']
		amount_invested = data['amount_invested']
		investment = Investment(investment_name, investment_type, amount_invested, amount_invested, 0)
		user.investments.append(investment)
		return jsonify({'message': 'Investment created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
