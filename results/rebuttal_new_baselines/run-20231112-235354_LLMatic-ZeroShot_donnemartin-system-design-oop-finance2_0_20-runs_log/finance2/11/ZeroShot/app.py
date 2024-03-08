from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}

@dataclass
class User:
	username: str
	password: str
	bank_accounts: list
	expenses: dict
	incomes: dict
	budgets: dict
	investments: dict

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, [], {}, {}, {}, {})
	return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
