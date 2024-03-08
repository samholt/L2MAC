from flask import Flask, request
from models.user import User
from models.transaction import Transaction
from models.budget import Budget
from models.investment import Investment
from models.alert import Alert

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'name' not in data or 'email' not in data or 'password' not in data:
		return {'message': 'Missing required fields'}, 400
	user = User.create_user(data['name'], data['email'], data['password'])
	return {'message': 'User created successfully'}, 201

@app.route('/authenticate_user', methods=['POST'])
def authenticate_user():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return {'message': 'Missing required fields'}, 400
	is_authenticated = User.authenticate_user(data['email'], data['password'])
	return {'authenticated': is_authenticated}

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	if 'user' not in data or 'bank_account' not in data:
		return {'message': 'Missing required fields'}, 400
	user = User()
	bank_accounts = user.link_bank_account(data['bank_account'])
	return {'bank_accounts': bank_accounts}

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	if 'user' not in data or 'amount' not in data or 'category' not in data or 'date' not in data:
		return {'message': 'Missing required fields'}, 400
	transaction = Transaction.create_transaction(data['user'], data['amount'], data['category'], data['date'])
	return {'message': 'Transaction created successfully'}, 201

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
	data = request.get_json()
	if 'user' not in data:
		return {'message': 'Missing required fields'}, 400
	transactions = Transaction.get_user_transactions(data['user'])
	return {'transactions': transactions}

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	if 'user' not in data or 'amount' not in data or 'category' not in data:
		return {'message': 'Missing required fields'}, 400
	budget = Budget.set_budget(data['user'], data['amount'], data['category'])
	return {'message': 'Budget set successfully'}, 201

@app.route('/adjust_budget', methods=['POST'])
def adjust_budget():
	data = request.get_json()
	if 'user' not in data or 'amount' not in data:
		return {'message': 'Missing required fields'}, 400
	budget = Budget.adjust_budget(data['user'], data['amount'])
	return {'message': 'Budget adjusted successfully'}, 201

@app.route('/get_budgets', methods=['GET'])
def get_budgets():
	data = request.get_json()
	if 'user' not in data:
		return {'message': 'Missing required fields'}, 400
	budgets = Budget.get_user_budgets(data['user'])
	return {'budgets': budgets}

@app.route('/link_investment_account', methods=['POST'])
def link_investment_account():
	data = request.get_json()
	if 'user' not in data or 'account' not in data:
		return {'message': 'Missing required fields'}, 400
	investment = Investment()
	account = investment.link_investment_account(data['account'])
	return {'message': 'Investment account linked successfully'}, 201

@app.route('/track_investment_performance', methods=['GET'])
def track_investment_performance():
	data = request.get_json()
	if 'user' not in data:
		return {'message': 'Missing required fields'}, 400
	investment_performance = Investment.track_investment_performance(data['user'])
	return {'investment_performance': investment_performance}

@app.route('/get_investments', methods=['GET'])
def get_investments():
	data = request.get_json()
	if 'user' not in data:
		return {'message': 'Missing required fields'}, 400
	investments = Investment.get_user_investments(data['user'])
	return {'investments': investments}

@app.route('/create_alert', methods=['POST'])
def create_alert():
	data = request.get_json()
	if 'user' not in data or 'alert_type' not in data or 'message' not in data:
		return {'message': 'Missing required fields'}, 400
	alert = Alert.create_alert(data['user'], data['alert_type'], data['message'])
	return {'message': 'Alert created successfully'}, 201

@app.route('/get_alerts', methods=['GET'])
def get_alerts():
	data = request.get_json()
	if 'user' not in data:
		return {'message': 'Missing required fields'}, 400
	alerts = Alert.get_user_alerts(data['user'])
	return {'alerts': alerts}

@app.route('/customize_alert', methods=['POST'])
def customize_alert():
	data = request.get_json()
	if 'user' not in data or 'alert_type' not in data or 'message' not in data:
		return {'message': 'Missing required fields'}, 400
	alert = Alert(data['user'], data['alert_type'], data['message'])
	custom_alert = alert.customize_alert(data['alert_type'], data['message'])
	return {'message': 'Alert customized successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
