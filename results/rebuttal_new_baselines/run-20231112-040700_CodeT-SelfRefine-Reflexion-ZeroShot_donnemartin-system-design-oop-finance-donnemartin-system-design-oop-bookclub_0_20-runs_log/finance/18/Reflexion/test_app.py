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
	return User(username='test', password='test')

@pytest.fixture
def sample_transaction():
	return Transaction(user_id='test', amount=100.0, category='groceries')


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_add_transaction(client, sample_transaction):
	response = client.post('/add_transaction', json=sample_transaction.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added'}


def test_get_transactions(client, sample_transaction):
	client.post('/add_transaction', json=sample_transaction.__dict__)
	client.post('/add_transaction', json=sample_transaction.__dict__)
	response = client.get(f'/get_transactions/{sample_transaction.user_id}')
	assert response.status_code == 200
	assert len(response.get_json()) == 2
