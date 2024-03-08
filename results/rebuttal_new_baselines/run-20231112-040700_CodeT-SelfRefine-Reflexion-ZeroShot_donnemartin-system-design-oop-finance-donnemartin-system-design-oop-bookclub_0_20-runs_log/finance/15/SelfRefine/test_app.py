import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={
		'id': '1',
		'username': 'test',
		'password': 'password'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == '1'

	# Test creating a user with the same username
	response = client.post('/create_user', json={
		'id': '2',
		'username': 'test',
		'password': 'password2'
	})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Username already exists'}

	# Test creating a user with invalid input data
	response = client.post('/create_user', json={
		'id': '3',
		'username': '',
		'password': 'password3'
	})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid input data'}


def test_create_transaction(client):
	response = client.post('/create_transaction', json={
		'id': '1',
		'user_id': '1',
		'amount': 100.0,
		'category': 'groceries',
		'recurring': False
	})
	assert response.status_code == 201
	assert json.loads(response.data) == '1'

	# Test creating a transaction with invalid input data
	response = client.post('/create_transaction', json={
		'id': '2',
		'user_id': '1',
		'amount': 'invalid',
		'category': 'groceries',
		'recurring': False
	})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid input data'}
