from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}

@dataclass
class User:
	username: str
	password: str
	budget: float = 0.0
	income: float = 0.0
	expenses: float = 0.0

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	users[username] = User(username, password)
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users and users[username].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/set_budget', methods=['POST'])
def set_budget():
	data = request.get_json()
	username = data['username']
	budget = data['budget']
	if username in users:
		users[username].budget = budget
		return jsonify({'message': 'Budget set successfully'}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/add_income', methods=['POST'])
def add_income():
	data = request.get_json()
	username = data['username']
	income = data['income']
	if username in users:
		users[username].income += income
		return jsonify({'message': 'Income added successfully'}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/add_expense', methods=['POST'])
def add_expense():
	data = request.get_json()
	username = data['username']
	expense = data['expense']
	if username in users:
		users[username].expenses += expense
		return jsonify({'message': 'Expense added successfully'}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/generate_report', methods=['GET'])
def generate_report():
	username = request.args.get('username')
	if username in users:
		user = users[username]
		report = {
			'username': user.username,
			'budget': user.budget,
			'income': user.income,
			'expenses': user.expenses,
			'remaining_budget': user.budget - user.expenses
		}
		return jsonify(report), 200
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
