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
	assert app.users_db['test'].username == 'test'
	assert app.users_db['test'].password == 'test'


def test_login(client):
	app.users_db['test'] = User('test', 'test')
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401


def test_add_transaction(client):
	app.users_db['test'] = User('test', 'test')
	response = client.post('/add_transaction', json={'user': 'test', 'type': 'income', 'amount': 1000, 'category': 'salary'})
	assert response.status_code == 201
	assert len(app.transactions_db['test']) == 1
	assert app.transactions_db['test'][0].amount == 1000
