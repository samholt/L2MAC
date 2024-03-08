from flask import Flask, request, jsonify
from account import Account
from expense_income import ExpenseIncome
from budget import Budget
from investment import Investment
from reports_alerts import ReportsAlerts

app = Flask(__name__)

account = Account()
expense_income = ExpenseIncome()
budget = Budget()
investment = Investment()
reports_alerts = ReportsAlerts()

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	account.create_account(data['user_id'], data['user_info'])
	return jsonify({'message': 'Account created successfully'}), 200

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	try:
		account.link_bank_account(data['user_id'], data['bank_account_info'])
		return jsonify({'message': 'Bank account linked successfully'}), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 400

@app.route('/handle_mfa', methods=['POST'])
def handle_mfa():
	data = request.get_json()
	try:
		account.handle_mfa(data['user_id'], data['mfa_info'])
		return jsonify({'message': 'MFA handled successfully'}), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 400

@app.route('/import_expenses_incomes', methods=['POST'])
def import_expenses_incomes():
	data = request.get_json()
	expense_income.import_expenses_incomes(data['user_id'], data['expenses'], data['incomes'])
	return jsonify({'message': 'Expenses and incomes imported successfully'}), 200

@app.route('/categorize_expenses_incomes', methods=['POST'])
def categorize_expenses_incomes():
	data = request.get_json()
	expense_income.categorize_expenses_incomes(data['user_id'], data['expense_categories'], data['income_categories'])
	return jsonify({'message': 'Expenses and incomes categorized successfully'}), 200

@app.route('/visualize_expense_income_history', methods=['GET'])
def visualize_expense_income_history():
	user_id = request.args.get('user_id')
	data = expense_income.visualize_expense_income_history(user_id)
	return jsonify(data), 200

@app.route('/set_adjust_budget', methods=['POST'])
def set_adjust_budget():
	data = request.get_json()
	budget.set_adjust_budget(data['user_id'], data['budget'])
	return jsonify({'message': 'Budget set/adjusted successfully'}), 200

@app.route('/alert_budget_limit', methods=['GET'])
def alert_budget_limit():
	user_id = request.args.get('user_id')
	message = budget.alert_budget_limit(user_id)
	return jsonify({'message': message}), 200

@app.route('/analyze_spending', methods=['GET'])
def analyze_spending():
	user_id = request.args.get('user_id')
	message = budget.analyze_spending(user_id)
	return jsonify({'message': message}), 200

@app.route('/integrate_investment_account', methods=['POST'])
def integrate_investment_account():
	data = request.get_json()
	investment.integrate_investment_account(data['user_id'], data['account_info'])
	return jsonify({'message': 'Investment account integrated successfully'}), 200

@app.route('/track_investment', methods=['POST'])
def track_investment():
	data = request.get_json()
	investment.track_investment(data['user_id'], data['investment_info'])
	return jsonify({'message': 'Investment tracked successfully'}), 200

@app.route('/overview_asset_allocation', methods=['POST'])
def overview_asset_allocation():
	data = request.get_json()
	investment.overview_asset_allocation(data['user_id'], data['allocation_info'])
	return jsonify({'message': 'Asset allocation overviewed successfully'}), 200

@app.route('/generate_report', methods=['POST'])
def generate_report():
	data = request.get_json()
	report = reports_alerts.generate_report(data['user_id'], data['report'])
	return jsonify(report), 200

@app.route('/custom_alert', methods=['POST'])
def custom_alert():
	data = request.get_json()
	alert = reports_alerts.custom_alert(data['user_id'], data['alert'])
	return jsonify({'alert': alert}), 200

if __name__ == '__main__':
	app.run(debug=True)
