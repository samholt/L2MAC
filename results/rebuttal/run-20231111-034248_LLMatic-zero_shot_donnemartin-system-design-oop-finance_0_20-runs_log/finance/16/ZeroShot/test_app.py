import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'username': 'test', 'password': 'test'}


def test_create_transaction(client):
	response = client.post('/create_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'is_recurring': False})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'is_recurring': False}


def test_create_account(client):
	response = client.post('/create_account', json={'id': '1', 'user_id': '1', 'balance': 1000.0})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'balance': 1000.0}


def test_create_budget(client):
	response = client.post('/create_budget', json={'id': '1', 'user_id': '1', 'category': 'groceries', 'limit': 500.0})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'category': 'groceries', 'limit': 500.0}


def test_create_investment(client):
	response = client.post('/create_investment', json={'id': '1', 'user_id': '1', 'value': 10000.0, 'roi': 0.05})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'value': 10000.0, 'roi': 0.05}
