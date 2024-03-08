from flask import Flask, request, jsonify
from controllers.user_controller import UserController
from controllers.transaction_controller import TransactionController
from controllers.budget_controller import BudgetController
from controllers.investment_controller import InvestmentController
from controllers.alert_controller import AlertController

app = Flask(__name__)

user_controller = UserController()
transaction_controller = TransactionController()
budget_controller = BudgetController()
investment_controller = InvestmentController()
alert_controller = AlertController()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.json
	user = user_controller.create_user(data['name'], data['email'], data['password'])
	return jsonify(user.to_dict()), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.json
	user = user_controller.authenticate(data['email'], data['password'])
	return jsonify(user.to_dict()), 200

@app.route('/transaction', methods=['POST', 'GET'])
def transaction():
	if request.method == 'POST':
		data = request.json
		transaction = transaction_controller.create_transaction(data['user_id'], data['amount'], data['type'], data['category'])
		return jsonify(transaction.to_dict()), 200
	else:
		transactions = transaction_controller.get_transactions(request.json)
		return jsonify([transaction.to_dict() for transaction in transactions]), 200

@app.route('/budget', methods=['POST', 'GET'])
def budget():
	if request.method == 'POST':
		data = request.json
		budget = budget_controller.create_budget(data['user_id'], data['amount'], data['category'], data['month'])
		return jsonify(budget.to_dict()), 200
	else:
		budgets = budget_controller.get_budgets(request.json)
		return jsonify([budget.to_dict() for budget in budgets]), 200

@app.route('/investment', methods=['POST', 'GET'])
def investment():
	if request.method == 'POST':
		data = request.json
		investment = investment_controller.create_investment(data['account_name'], data['balance'], data['asset_allocation'])
		return jsonify(investment.to_dict()), 200
	else:
		investments = investment_controller.get_investments(request.json)
		return jsonify([investment.to_dict() for investment in investments]), 200

@app.route('/create_alert', methods=['POST'])
def create_alert():
	data = request.json
	alert = alert_controller.create_alert(data['user_id'], data['message'])
	return jsonify(alert.to_dict()), 201

@app.route('/get_user_alerts', methods=['GET'])
def get_user_alerts():
	data = request.args
	alerts = alert_controller.get_alerts(data['user_id'])
	return jsonify({'alerts': [alert.to_dict() for alert in alerts]}), 200

if __name__ == '__main__':
	app.run(debug=True)
