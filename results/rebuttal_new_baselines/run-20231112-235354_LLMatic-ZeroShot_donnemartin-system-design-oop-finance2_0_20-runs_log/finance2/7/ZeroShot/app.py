from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users_db = {}

@dataclass
class User:
	username: str
	password: str
	bank_accounts: Dict[str, str] = {}
	expenses: Dict[str, float] = {}
	incomes: Dict[str, float] = {}
	budgets: Dict[str, float] = {}
	investments: Dict[str, float] = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username, password)
	users_db[username] = user
	return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
