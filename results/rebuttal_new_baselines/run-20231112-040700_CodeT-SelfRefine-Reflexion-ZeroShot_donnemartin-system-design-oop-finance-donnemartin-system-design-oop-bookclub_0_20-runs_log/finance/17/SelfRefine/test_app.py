import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_add_transaction(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_transaction', json={'user': 'test', 'password': 'test', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added'}


def test_add_transaction_invalid_password(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_transaction', json={'user': 'test', 'password': 'wrong', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}
