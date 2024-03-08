import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'


def test_add_transaction(client):
	response = client.post('/add_transaction', data=json.dumps({'user_id': 'test', 'type': 'income', 'amount': 1000, 'category': 'salary'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Transaction added successfully'
