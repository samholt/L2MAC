from flask import Flask, request, jsonify
from user import User
from security import hash_password, verify_password, generate_otp
from expenses import Expense
from incomes import Income
from categorization import categorize_expense, categorize_income
from visualization import visualize_expense_income_history
from budget import Budget
from analysis import analyze_spending_pattern
from investment import Investment
from reports import Reports

app = Flask(__name__)

users = {}
expenses = {}
incomes = {}
budgets = {}
investments = {}
reports = Reports()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, hash_password(password))
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users.get(username)
	if user and verify_password(user.password, password):
		return jsonify({'message': 'Login successful', 'otp': generate_otp()}), 200
	return jsonify({'message': 'Invalid username or password'}), 400

@app.route('/expense', methods=['POST'])
def add_expense():
	data = request.get_json()
	username = data['username']
	expense_id = data['id']
	amount = data['amount']
	category = categorize_expense(amount)
	date = data['date']
	expenses[expense_id] = Expense(expense_id, amount, category, date)
	return jsonify({'message': 'Expense added successfully'}), 200

@app.route('/income', methods=['POST'])
def add_income():
	data = request.get_json()
	username = data['username']
	income_id = data['id']
	amount = data['amount']
	source = categorize_income(data['source'])
	date = data['date']
	incomes[income_id] = Income(income_id, amount, source, date)
	return jsonify({'message': 'Income added successfully'}), 200

@app.route('/budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	username = data['username']
	monthly_budget = data['monthly_budget']
	budgets[username] = Budget(monthly_budget)
	return jsonify({'message': 'Budget set successfully'}), 200

@app.route('/investment', methods=['POST'])
def integrate_investment():
	data = request.get_json()
	username = data['username']
	investment_info = data['investment_info']
	investments[username] = Investment(investment_info)
	return jsonify({'message': 'Investment integrated successfully'}), 200

@app.route('/report', methods=['GET'])
def get_report():
	username = request.args.get('username')
	report_type = request.args.get('type')
	if report_type == 'monthly_summary':
		reports.generate_monthly_summary(users[username])
	elif report_type == 'alerts':
		reports.generate_alerts(users[username])
	return jsonify({'report': reports.get_report(report_type)}), 200

if __name__ == '__main__':
	app.run(debug=True)
