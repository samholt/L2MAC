import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return User('test_user', 'test_password')

@pytest.fixture
def sample_transaction():
	return Transaction('test_user', 'groceries', 100.0)


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_add_transaction(client, sample_user, sample_transaction):
	client.post('/create_user', json=sample_user.__dict__)
	response = client.post('/add_transaction', json=sample_transaction.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added'}


def test_add_transaction_no_user(client, sample_transaction):
	response = client.post('/add_transaction', json=sample_transaction.__dict__)
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}


def test_create_existing_user(client, sample_user):
	client.post('/create_user', json=sample_user.__dict__)
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}
