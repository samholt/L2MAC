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


def test_register(client, sample_user):
	response = client.post('/register', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == sample_user.__dict__


def test_login(client, sample_user):
	app.users[sample_user.id] = sample_user
	response = client.post('/login', json={'id': sample_user.id, 'password': sample_user.password})
	assert response.status_code == 200
	assert response.get_json() == sample_user.__dict__


def test_add_transaction(client, sample_transaction):
	response = client.post('/transactions', json=sample_transaction.__dict__)
	assert response.status_code == 201
	assert response.get_json() == sample_transaction.__dict__


def test_get_transactions(client, sample_transaction):
	app.transactions[sample_transaction.id] = sample_transaction
	response = client.get('/transactions', query_string={'user_id': sample_transaction.user_id})
	assert response.status_code == 200
	assert response.get_json() == [sample_transaction.__dict__]
