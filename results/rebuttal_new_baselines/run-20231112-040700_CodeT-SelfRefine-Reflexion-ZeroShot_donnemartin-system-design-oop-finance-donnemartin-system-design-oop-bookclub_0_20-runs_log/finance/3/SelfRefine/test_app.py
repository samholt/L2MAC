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
	assert json.loads(response.data) == '1'

	# Test creating a user with the same ID
	response = client.post('/create_user', json={'id': '1', 'username': 'test2', 'password': 'test2'})
	assert response.status_code == 400
	assert json.loads(response.data) == 'A user with this ID already exists'


def test_add_transaction(client):
	response = client.post('/add_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert json.loads(response.data) == '1'

	# Test adding a transaction with the same ID
	response = client.post('/add_transaction', json={'id': '1', 'user_id': '2', 'amount': 200.0, 'category': 'rent'})
	assert response.status_code == 400
	assert json.loads(response.data) == 'A transaction with this ID already exists'
