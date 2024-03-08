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
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200


def test_link_bank_account(client):
	response = client.post('/link_bank_account', json={'user_id': '1', 'bank_account': '1234567890'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200


def test_add_expense(client):
	response = client.post('/add_expense', json={'user_id': '1', 'expense': {'category': 'food', 'amount': 100}})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200


def test_add_income(client):
	response = client.post('/add_income', json={'user_id': '1', 'income': {'source': 'salary', 'amount': 1000}})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200


def test_set_budget(client):
	response = client.post('/set_budget', json={'user_id': '1', 'budget': {'food': 500, 'rent': 1000}})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200


def test_add_investment(client):
	response = client.post('/add_investment', json={'user_id': '1', 'investment': {'type': 'stocks', 'amount': 10000}})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200
