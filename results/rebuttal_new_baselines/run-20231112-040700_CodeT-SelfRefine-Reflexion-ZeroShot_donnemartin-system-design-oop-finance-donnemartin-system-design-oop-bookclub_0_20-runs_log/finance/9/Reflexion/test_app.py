import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully.'}
	assert isinstance(app.users['john@example.com'], User)

	response = client.post('/create_user', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists.'}

	response = client.post('/create_user', json={'name': 'John', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid data.'}


def test_create_transaction(client):
	app.users['john@example.com'] = User('John', 'john@example.com', 'password')

	response = client.post('/create_transaction', json={'user_email': 'john@example.com', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction created successfully.'}
	assert isinstance(app.transactions['john@example.com'], Transaction)

	response = client.post('/create_transaction', json={'user_email': 'jane@example.com', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User does not exist.'}

	response = client.post('/create_transaction', json={'user_email': 'john@example.com', 'amount': 100.0})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid data.'}
