import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test123'})
	assert response.status_code == 201
	assert app.users_db['test'].username == 'test'
	assert app.users_db['test'].password == 'test123'


def test_add_transaction(client):
	response = client.post('/add_transaction', json={'user_id': 'test', 'type': 'income', 'amount': 1000.0, 'category': 'salary'})
	assert response.status_code == 201
	assert app.transactions_db['test'].user_id == 'test'
	assert app.transactions_db['test'].type == 'income'
	assert app.transactions_db['test'].amount == 1000.0
	assert app.transactions_db['test'].category == 'salary'
