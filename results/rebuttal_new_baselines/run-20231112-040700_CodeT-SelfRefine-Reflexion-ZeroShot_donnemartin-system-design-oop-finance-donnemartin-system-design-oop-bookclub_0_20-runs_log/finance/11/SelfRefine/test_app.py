import pytest
import app
from app import User, Transaction
from werkzeug.security import generate_password_hash, check_password_hash

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
	return {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'password': 'test'}


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert check_password_hash(app.users_db[sample_user.id].password, sample_user.password)


def test_create_transaction(client, sample_transaction):
	response = client.post('/create_transaction', json=sample_transaction)
	assert response.status_code == 201
	assert app.transactions_db[sample_transaction['id']].user_id == sample_transaction['user_id']
