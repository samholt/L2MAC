import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'id': '1', 'username': 'test', 'password': 'test', 'bank_accounts': [], 'expenses': {}, 'incomes': {}, 'budgets': {}, 'investments': {}}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_link_bank_account(client):
	response = client.post('/link_bank_account', data=json.dumps({'user_id': '1', 'bank_account': '1234567890'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Bank account linked successfully'}


def test_add_expense(client):
	response = client.post('/add_expense', data=json.dumps({'user_id': '1', 'expense': {'category': 'Food', 'amount': 100}}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Expense added successfully'}


def test_add_income(client):
	response = client.post('/add_income', data=json.dumps({'user_id': '1', 'income': {'source': 'Salary', 'amount': 1000}}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Income added successfully'}


def test_set_budget(client):
	response = client.post('/set_budget', data=json.dumps({'user_id': '1', 'budget': {'category': 'Food', 'amount': 500}}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Budget set successfully'}


def test_add_investment(client):
	response = client.post('/add_investment', data=json.dumps({'user_id': '1', 'investment': {'type': 'Stock', 'amount': 1000}}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Investment added successfully'}
