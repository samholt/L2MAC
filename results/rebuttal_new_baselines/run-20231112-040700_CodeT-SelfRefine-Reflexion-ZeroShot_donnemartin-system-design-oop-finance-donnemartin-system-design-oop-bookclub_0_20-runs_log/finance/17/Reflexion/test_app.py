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
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_add_transaction(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_transaction', json={'username': 'test', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}
