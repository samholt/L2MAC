import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.data == b'Hello, World!'


def test_register(client):
	response = client.post('/register', json={'name': 'test', 'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 200


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 200


def test_transaction(client):
	response = client.post('/transaction', json={'user_id': 1, 'amount': 100, 'type': 'income', 'category': 'salary'})
	assert response.status_code == 200
	response = client.get('/transaction', json={'user_id': 1})
	assert response.status_code == 200


def test_budget(client):
	response = client.post('/budget', json={'user_id': 1, 'amount': 1000, 'category': 'groceries', 'month': 'January'})
	assert response.status_code == 200
	response = client.get('/budget', json={'user_id': 1})
	assert response.status_code == 200


def test_investment(client):
	response = client.post('/investment', json={'account_name': 'Savings', 'balance': 1000, 'asset_allocation': {'stocks': 50, 'bonds': 50}})
	assert response.status_code == 200
	response = client.get('/investment', json={'user_id': 1})
	assert response.status_code == 200


def test_alert(client):
	response = client.post('/create_alert', json={'user_id': 1, 'message': 'Test alert'})
	assert response.status_code == 201
	response = client.get('/get_user_alerts', json={'user_id': 1})
	assert response.status_code == 200
	assert 'alerts' in response.get_json()
	assert len(response.get_json()['alerts']) >= 1
