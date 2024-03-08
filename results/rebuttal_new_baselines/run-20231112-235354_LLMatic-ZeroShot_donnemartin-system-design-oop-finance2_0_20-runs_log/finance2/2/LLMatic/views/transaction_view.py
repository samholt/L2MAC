from flask import request, jsonify
from models.transaction import Transaction


def create_transaction():
	data = request.get_json()
	transaction = Transaction.create(data['user'], data['amount'], data['type'], data['category'])
	return jsonify({'message': 'Transaction created successfully'}), 201

def get_transactions():
	data = request.get_json()
	transactions = Transaction.get_transactions(data['user'])
	return jsonify({'transactions': transactions}), 200
