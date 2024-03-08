import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	data = {'id': '1', 'username': 'test', 'password': 'test'}
	response = client.post('/create_user', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data


def test_create_account(client):
	data = {'id': '1', 'user_id': '1', 'balance': 1000.0}
	response = client.post('/create_account', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data


def test_create_transaction(client):
	data = {'id': '1', 'account_id': '1', 'amount': 100.0, 'category': 'groceries'}
	response = client.post('/create_transaction', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data
