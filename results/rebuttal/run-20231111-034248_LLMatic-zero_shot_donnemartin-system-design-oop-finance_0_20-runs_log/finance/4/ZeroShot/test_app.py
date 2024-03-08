import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'test' in app.users


def test_login(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_add_transaction(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/transaction', json={'user_id': 'test', 'type': 'income', 'amount': 1000.0, 'category': 'salary'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}
	assert 'test' in app.transactions
	assert isinstance(app.transactions['test'][0], Transaction)
