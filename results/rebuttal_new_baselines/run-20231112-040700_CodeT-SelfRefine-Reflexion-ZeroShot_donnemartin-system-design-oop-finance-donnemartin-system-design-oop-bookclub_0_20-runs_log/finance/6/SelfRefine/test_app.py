import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

	# Test creating a user with a duplicate username
	response = client.post('/create_user', json={'id': '2', 'username': 'test', 'password': 'test2'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Username already exists'}

	# Test creating a user with missing fields
	response = client.post('/create_user', json={'id': '3', 'username': 'test3'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Missing required field'}


def test_create_transaction(client):
	response = client.post('/create_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

	# Test creating a transaction with a duplicate id
	response = client.post('/create_transaction', json={'id': '1', 'user_id': '2', 'amount': 200.0, 'category': 'rent', 'recurring': True})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Transaction already exists'}

	# Test creating a transaction with missing fields
	response = client.post('/create_transaction', json={'id': '2', 'user_id': '2', 'amount': 200.0, 'category': 'rent'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Missing required field'}
