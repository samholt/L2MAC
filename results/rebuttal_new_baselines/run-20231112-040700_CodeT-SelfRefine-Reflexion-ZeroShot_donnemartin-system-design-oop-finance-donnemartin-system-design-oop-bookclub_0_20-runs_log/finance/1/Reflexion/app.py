from flask import Flask, request
from models import User, Transaction

app = Flask(__name__)

users = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'message': 'User created successfully'}, 201

@app.route('/add_transaction/<user_id>', methods=['POST'])
def add_transaction(user_id):
	data = request.get_json()
	transaction = Transaction(**data)
	users[user_id].transactions.append(transaction)
	return {'message': 'Transaction added successfully'}, 201
