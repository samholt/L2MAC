from flask import Flask, request, render_template
from user import User
from transaction import Transaction
from account import Account
from investment import Investment

app = Flask(__name__)

users = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	users[data['username']] = User(data['username'], data['password'], data['email'])
	return {'message': 'User created successfully'}, 201

@app.route('/authenticate', methods=['POST'])
def authenticate():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'message': 'Authentication successful'}, 200
	return {'message': 'Authentication failed'}, 401

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		return {'password': user.recover_password()}, 200
	return {'message': 'User not found'}, 404

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		user.set_budget(data['category'], data['amount'])
		return {'message': 'Budget set successfully'}, 200
	return {'message': 'Failed to set budget'}, 400

@app.route('/check_budget', methods=['POST'])
def check_budget():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'over_budget': user.check_budget(data['category'])}, 200
	return {'message': 'Failed to check budget'}, 400

@app.route('/track_progress', methods=['POST'])
def track_progress():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'progress': user.track_progress(data['category'])}, 200
	return {'message': 'Failed to track progress'}, 400

@app.route('/generate_monthly_report', methods=['POST'])
def generate_monthly_report():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'report': user.generate_monthly_report(data['month'], data['year'])}, 200
	return {'message': 'Failed to generate report'}, 400

@app.route('/visualize_spending_habits', methods=['POST'])
def visualize_spending_habits():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'spending': user.visualize_spending_habits()}, 200
	return {'message': 'Failed to visualize spending habits'}, 400

@app.route('/compare_year_on_year', methods=['POST'])
def compare_year_on_year():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'comparison': user.compare_year_on_year(data['year1'], data['year2'])}, 200
	return {'message': 'Failed to compare year on year'}, 400

@app.route('/get_savings_tips', methods=['POST'])
def get_savings_tips():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'tips': user.get_savings_tips()}, 200
	return {'message': 'Failed to get savings tips'}, 400

@app.route('/get_product_recommendations', methods=['POST'])
def get_product_recommendations():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'recommendations': user.get_product_recommendations()}, 200
	return {'message': 'Failed to get product recommendations'}, 400

@app.route('/get_notifications', methods=['POST'])
def get_notifications():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.authenticate(data['password']):
		return {'notifications': user.get_notifications()}, 200
	return {'message': 'Failed to get notifications'}, 400

if __name__ == '__main__':
	app.run(debug=True)

