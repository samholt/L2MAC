from flask import Flask, request, jsonify
from account import User
from expense_income import Expense, Income
from budget import Budget
from investment import Investment
from reports import Reports

app = Flask(__name__)

# Initialize the classes
user = User('', '')
expense = Expense(0, '')
income = Income(0, '')
budget = Budget(0)
investment = Investment()
reports = Reports()

@app.route('/create_user', methods=['POST'])
def create_user():
	# Get the data from the request
	data = request.get_json()
	# Create a new user
	user.create_user(data['username'], data['password'])
	# Send the authentication code to the user's email
	user.send_auth_code(data['email'])
	return jsonify({'message': 'User created successfully'}), 200

@app.route('/authenticate_user', methods=['POST'])
def authenticate_user():
	data = request.get_json()
	# Authenticate the user
	if user.authenticate_user(data['username'], data['password'], data['auth_code']):
		return jsonify({'message': 'User authenticated successfully'}), 200
	else:
		return jsonify({'message': 'Authentication failed'}), 401

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	# Link the user's bank account
	user.link_bank_account(data['account_number'])
	return jsonify({'message': 'Bank account linked successfully'}), 200

@app.route('/add_expense', methods=['POST'])
def add_expense():
	data = request.get_json()
	# Add an expense
	expense.add_expense(data['amount'], data['category'])
	return jsonify({'message': 'Expense added successfully'}), 200

@app.route('/add_income', methods=['POST'])
def add_income():
	data = request.get_json()
	# Add an income
	income.add_income(data['amount'], data['category'])
	return jsonify({'message': 'Income added successfully'}), 200

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	# Set the budget
	budget.set_budget(data['new_budget'])
	return jsonify({'message': 'Budget set successfully'}), 200

@app.route('/adjust_budget', methods=['POST'])
def adjust_budget():
	data = request.get_json()
	# Adjust the budget
	budget.adjust_budget(data['adjustment'])
	return jsonify({'message': 'Budget adjusted successfully'}), 200

@app.route('/link_investment_account', methods=['POST'])
def link_investment_account():
	data = request.get_json()
	# Link the investment account
	investment.link_account(data['account_name'], data['account'])
	return jsonify({'message': 'Investment account linked successfully'}), 200

@app.route('/track_investment_performance', methods=['POST'])
def track_investment_performance():
	data = request.get_json()
	# Track the performance of the investment
	investment.track_performance(data['account_name'], data['performance'])
	return jsonify({'message': 'Investment performance tracked successfully'}), 200

@app.route('/generate_report', methods=['GET'])
def generate_report():
	# Get the month from the request parameters
	month = request.args.get('month')
	# Generate the report
	report = reports.generate_report(month)
	if report == 'No data for this month':
		return jsonify({'message': report}), 404
	else:
		return jsonify({'report': report}), 200

if __name__ == '__main__':
	app.run(debug=True)
