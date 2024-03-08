from flask import request, jsonify
from models.investment import Investment


def create_investment():
	data = request.get_json()
	investment = Investment(data['account_name'], data['balance'], data['asset_allocation'])
	return jsonify({'message': 'Investment created successfully'}), 201

def view_asset_allocation():
	data = request.get_json()
	investment = Investment(data['account_name'], data['balance'], data['asset_allocation'])
	asset_allocation = investment.view_asset_allocation()
	return jsonify({'asset_allocation': asset_allocation}), 200
