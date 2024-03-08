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


def test_add_transaction(client):
	response = client.post('/add_transaction', json={'user_id': 'test', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 201
	assert app.transactions['test'].category == 'groceries'
