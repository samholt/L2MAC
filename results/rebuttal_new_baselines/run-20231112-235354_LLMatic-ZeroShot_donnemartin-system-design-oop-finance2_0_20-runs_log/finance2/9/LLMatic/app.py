from flask import Flask, request
from models.user import User
from models.transaction import Transaction
from models.budget import Budget
from models.investment import Investment
from models.alert import Alert

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	if user.authenticate(data['password']):
		return {'message': 'Login successful'}, 200
	else:
		return {'message': 'Invalid credentials'}, 401

@app.route('/transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction.create(data['user'], data['amount'], data['type'], data['category'])
	return {'message': 'Transaction created successfully'}, 201

@app.route('/budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	budget = Budget(data['user'], data['amount'], data['category'])
	return {'message': 'Budget set successfully'}, 201

@app.route('/investment', methods=['POST'])
def link_investment():
	data = request.get_json()
	investment = Investment(data['user'], data['type'], data['amount'], data['performance'])
	investment.link_investment_account(data['account'])
	return {'message': 'Investment account linked successfully'}, 201

@app.route('/alert', methods=['POST'])
def set_alert():
	data = request.get_json()
	alert = Alert(data['user'], data['alert_type'], data['message'])
	alert.send_alert()
	return {'message': 'Alert set and sent successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
