import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'username': 'test', 'password': 'test'},
])
def test_create_user(client, user):
	response = client.post('/create_user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == user['id']

@pytest.mark.parametrize('transaction', [
	{'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False},
])
def test_create_transaction(client, transaction):
	response = client.post('/create_transaction', data=json.dumps(transaction), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == transaction['id']

@pytest.mark.parametrize('bank_account', [
	{'id': '1', 'user_id': '1', 'balance': 1000.0},
])
def test_create_bank_account(client, bank_account):
	response = client.post('/create_bank_account', data=json.dumps(bank_account), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == bank_account['id']

@pytest.mark.parametrize('budget', [
	{'id': '1', 'user_id': '1', 'category': 'groceries', 'limit': 500.0},
])
def test_create_budget(client, budget):
	response = client.post('/create_budget', data=json.dumps(budget), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == budget['id']

@pytest.mark.parametrize('investment', [
	{'id': '1', 'user_id': '1', 'value': 10000.0},
])
def test_create_investment(client, investment):
	response = client.post('/create_investment', data=json.dumps(investment), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == investment['id']
