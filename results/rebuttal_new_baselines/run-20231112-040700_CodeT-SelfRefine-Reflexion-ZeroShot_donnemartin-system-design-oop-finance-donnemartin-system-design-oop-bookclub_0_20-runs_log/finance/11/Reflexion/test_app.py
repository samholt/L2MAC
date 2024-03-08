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
	assert app.users['test'].username == 'test'
	assert app.users['test'].password == 'test'


def test_add_transaction(client):
	app.users['test'] = User('test', 'test')
	response = client.post('/add_transaction', json={'user_id': 'test', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert app.transactions['test'].user_id == 'test'
	assert app.transactions['test'].amount == 100.0
	assert app.transactions['test'].category == 'groceries'
