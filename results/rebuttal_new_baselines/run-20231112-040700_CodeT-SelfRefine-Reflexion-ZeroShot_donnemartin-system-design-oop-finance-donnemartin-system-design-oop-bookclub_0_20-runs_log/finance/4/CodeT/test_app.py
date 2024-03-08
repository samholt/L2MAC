import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_login(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_add_transaction(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_transaction', json={'user_id': 'test', 'type': 'income', 'amount': 1000.0, 'category': 'salary'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Transaction added successfully'}
