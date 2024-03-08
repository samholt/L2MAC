import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}
	assert isinstance(app.users['test'], User)

def test_login(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_add_transaction(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/add_transaction', json={'username': 'test', 'amount': 100, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}
	assert isinstance(app.transactions['test'][0], Transaction)

	response = client.post('/add_transaction', json={'username': 'wrong', 'amount': 100, 'category': 'groceries'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User does not exist'}

def test_get_transactions(client):
	app.users['test'] = User('test', 'test')
	app.transactions['test'] = [Transaction('test', 100, 'groceries')]
	response = client.get('/get_transactions', query_string={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == [{'username': 'test', 'amount': 100.0, 'category': 'groceries'}]

	response = client.get('/get_transactions', query_string={'username': 'wrong'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User does not exist'}
