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
	return User(id='1', username='test', password='test')

@pytest.fixture
def sample_transaction():
	return Transaction(id='1', user_id='1', amount=100.0, category='groceries')


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert app.DATABASE[sample_user.id] == sample_user


def test_add_transaction(client, sample_transaction):
	response = client.post('/add_transaction', json=sample_transaction.__dict__)
	assert response.status_code == 201
	assert app.DATABASE[sample_transaction.id] == sample_transaction
