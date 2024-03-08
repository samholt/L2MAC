from flask import request, jsonify
from models.budget import Budget


def create_budget():
	data = request.get_json()
	budget = Budget(data['user'], data['amount'], data['category'], data['month'])
	return jsonify({'message': 'Budget created successfully'}), 201

def adjust_budget():
	data = request.get_json()
	budget = Budget(data['user'], data['amount'], data['category'], data['month'])
	budget.adjust_budget(data['amount'])
	return jsonify({'message': 'Budget adjusted successfully'}), 200
