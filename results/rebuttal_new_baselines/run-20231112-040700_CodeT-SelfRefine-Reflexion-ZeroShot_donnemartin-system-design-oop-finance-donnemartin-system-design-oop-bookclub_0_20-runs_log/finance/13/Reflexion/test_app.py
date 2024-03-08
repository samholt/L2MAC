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
	assert b'User created' in response.data


def test_add_transaction(client):
	data = {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'}
	response = client.post('/add_transaction', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert b'Transaction added' in response.data
