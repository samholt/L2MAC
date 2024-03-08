from flask import Flask, request, jsonify
from user import UserManager
from transaction import TransactionManager
from bank_account import BankAccountManager
from budget import BudgetManager, Budget
from investment import InvestmentManager
from report import ReportManager
from recommendation import RecommendationManager
from notification import NotificationManager

app = Flask(__name__)

user_manager = UserManager()
transaction_manager = TransactionManager()
bank_account_manager = BankAccountManager()
budget_manager = BudgetManager()
investment_manager = InvestmentManager()
report_manager = ReportManager()
recommendation_manager = RecommendationManager()
notification_manager = NotificationManager()

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	email = data.get('email')
	user = user_manager.create_user(username, password, email)
	if user:
		return jsonify({'message': 'User created'}), 201
	else:
		return jsonify({'message': 'User already exists'}), 400

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = user_manager.users.get(username)
	if user:
		return jsonify({'username': user.username, 'email': user.email}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	id = data.get('id')
	amount = data.get('amount')
	date = data.get('date')
	type = data.get('type')
	transaction_manager.add_transaction(id, amount, date, type)
	return jsonify({'message': 'Transaction added'}), 201

@app.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
	transaction = transaction_manager.get_transaction(id)
	if transaction:
		return jsonify({'id': transaction.id, 'amount': transaction.amount, 'date': transaction.date, 'type': transaction.type}), 200
	else:
		return jsonify({'message': 'Transaction not found'}), 404

@app.route('/bank_account', methods=['POST'])
def link_account():
	data = request.get_json()
	account_number = data.get('account_number')
	bank_account_manager.link_account(account_number)
	return jsonify({'message': 'Bank account linked'}), 201

@app.route('/bank_account/<account_number>', methods=['GET'])
def get_bank_account(account_number):
	bank_account = bank_account_manager.bank_accounts.get(account_number)
	if bank_account:
		return jsonify({'account_number': bank_account.account_number, 'balance': bank_account.balance}), 200
	else:
		return jsonify({'message': 'Bank account not found'}), 404

@app.route('/budget', methods=['POST'])
def add_budget():
	data = request.get_json()
	category = data.get('category')
	limit = data.get('limit')
	budget_manager.add_budget(Budget(category, limit))
	return jsonify({'message': 'Budget added'}), 201

@app.route('/budget/<category>', methods=['GET'])
def get_budget(category):
	budget = budget_manager.get_budget(category)
	if budget:
		return jsonify({'category': budget.category, 'limit': budget.limit, 'total_spent': budget.get_total_spent(), 'remaining_budget': budget.get_remaining_budget()}), 200
	else:
		return jsonify({'message': 'Budget not found'}), 404

@app.route('/investment', methods=['POST'])
def add_investment():
	data = request.get_json()
	name = data.get('name')
	quantity = data.get('quantity')
	purchase_price = data.get('purchase_price')
	current_price = data.get('current_price')
	investment_manager.add_investment(name, quantity, purchase_price, current_price)
	return jsonify({'message': 'Investment added'}), 201

@app.route('/investment/<name>', methods=['GET'])
def get_investment(name):
	investment = investment_manager.investments.get(name)
	if investment:
		return jsonify({'name': investment.name, 'quantity': investment.quantity, 'purchase_price': investment.purchase_price, 'current_price': investment.current_price, 'performance': investment.track_performance()}), 200
	else:
		return jsonify({'message': 'Investment not found'}), 404

@app.route('/report', methods=['POST'])
def create_report():
	data = request.get_json()
	username = data.get('username')
	month = data.get('month')
	income = data.get('income')
	expenses = data.get('expenses')
	savings = data.get('savings')
	investments = data.get('investments')
	user = user_manager.users.get(username)
	if user:
		report_manager.create_report(user, month, income, expenses, savings, investments)
		return jsonify({'message': 'Report created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/report/<username>/<month>', methods=['GET'])
def get_report(username, month):
	report = report_manager.get_report(username, month)
	if report:
		return jsonify(report.generate_monthly_report()), 200
	else:
		return jsonify({'message': 'Report not found'}), 404

@app.route('/recommendation', methods=['POST'])
def create_recommendation():
	data = request.get_json()
	username = data.get('username')
	user = user_manager.users.get(username)
	if user:
		recommendation_manager.create_recommendation(user)
		return jsonify({'message': 'Recommendation created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/recommendation/<username>', methods=['GET'])
def get_recommendation(username):
	recommendation = recommendation_manager.get_recommendation(username)
	if recommendation:
		return jsonify({'username': recommendation.user.username, 'tips': recommendation.tips, 'financial_products': recommendation.financial_products}), 200
	else:
		return jsonify({'message': 'Recommendation not found'}), 404

@app.route('/notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	username = data.get('username')
	message = data.get('message')
	user = user_manager.users.get(username)
	if user:
		notification_manager.create_notification(user, message)
		return jsonify({'message': 'Notification created'}), 201
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
