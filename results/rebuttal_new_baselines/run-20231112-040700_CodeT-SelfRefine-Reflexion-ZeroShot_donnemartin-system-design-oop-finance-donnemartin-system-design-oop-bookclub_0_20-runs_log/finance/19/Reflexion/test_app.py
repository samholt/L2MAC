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
	return User(id='1', email='test@test.com', password='password')

@pytest.fixture
def sample_transaction():
	return Transaction(id='1', user_id='1', amount=100.0, category='groceries')


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_add_transaction(client, sample_transaction):
	response = client.post('/add_transaction', json=sample_transaction.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}


def test_get_transactions(client, sample_user, sample_transaction):
	client.post('/create_user', json=sample_user.__dict__)
	client.post('/add_transaction', json=sample_transaction.__dict__)
	response = client.get(f'/get_transactions/{sample_user.id}')
	assert response.status_code == 200
	assert response.get_json() == {'transactions': [sample_transaction.__dict__]}


def test_delete_user(client, sample_user):
	client.post('/create_user', json=sample_user.__dict__)
	response = client.delete(f'/delete_user/{sample_user.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User deleted successfully'}


def test_delete_transaction(client, sample_transaction):
	client.post('/add_transaction', json=sample_transaction.__dict__)
	response = client.delete(f'/delete_transaction/{sample_transaction.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Transaction deleted successfully'}
