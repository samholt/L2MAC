from flask import request, jsonify
from models.transaction import Transaction


def create_transaction():
	data = request.get_json()
	transaction = Transaction.create_transaction(data['user'], data['amount'], data['category'])
	return jsonify({'message': 'Transaction created successfully', 'transaction': transaction.__dict__}), 201


def get_user_transactions():
	user = request.args.get('user')
	transactions = Transaction.get_user_transactions()
	return jsonify({'transactions': [transaction.__dict__ for transaction in transactions]}), 200


def categorize_transactions():
	data = request.get_json()
	transactions = Transaction.categorize_transactions()
	return jsonify({'transactions': [transaction.__dict__ for transaction in transactions]}), 200

