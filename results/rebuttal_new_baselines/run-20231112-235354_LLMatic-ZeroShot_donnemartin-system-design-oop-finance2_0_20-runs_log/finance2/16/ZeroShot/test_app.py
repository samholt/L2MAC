import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test', 'bank_accounts': [], 'expenses': {}, 'incomes': {}, 'budgets': {}, 'investments': {}})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_link_bank_account(client):
	response = client.post('/link_bank_account', json={'user_id': '1', 'bank_account': '1234567890'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Bank account linked successfully'}


def test_add_expense(client):
	response = client.post('/add_expense', json={'user_id': '1', 'expense': {'category': 'Food', 'amount': 100}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Expense added successfully'}


def test_add_income(client):
	response = client.post('/add_income', json={'user_id': '1', 'income': {'source': 'Salary', 'amount': 1000}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Income added successfully'}


def test_set_budget(client):
	response = client.post('/set_budget', json={'user_id': '1', 'budget': {'category': 'Food', 'amount': 500}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Budget set successfully'}


def test_add_investment(client):
	response = client.post('/add_investment', json={'user_id': '1', 'investment': {'type': 'Stocks', 'amount': 10000}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Investment added successfully'}
