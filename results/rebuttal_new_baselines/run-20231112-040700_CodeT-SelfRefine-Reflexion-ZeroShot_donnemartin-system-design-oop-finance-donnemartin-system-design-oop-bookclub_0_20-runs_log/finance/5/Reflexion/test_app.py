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
	assert 'test' in app.users
	assert app.users['test'] == User('test', 'test')

def test_login(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_add_transaction(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/add_transaction', json={'username': 'test', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}
	assert 'test' in app.transactions
	assert app.transactions['test'] == [Transaction('test', 100.0, 'groceries')]

	response = client.post('/add_transaction', json={'username': 'wrong', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
