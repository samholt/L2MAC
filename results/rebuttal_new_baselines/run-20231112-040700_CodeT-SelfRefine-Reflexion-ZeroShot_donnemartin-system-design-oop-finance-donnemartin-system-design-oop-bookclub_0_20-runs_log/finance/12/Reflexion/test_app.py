import pytest
import app
from models.user import User
from models.transaction import Transaction
from models.account import Account
from models.budget import Budget
from models.investment import Investment

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_transaction(client):
	response = client.post('/transaction', json={'id': 1, 'user_id': 1, 'account_id': 1, 'amount': 100.0, 'category': 'groceries', 'is_recurring': False})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_account(client):
	response = client.post('/account', json={'id': 1, 'user_id': 1, 'balance': 1000.0})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_budget(client):
	response = client.post('/budget', json={'id': 1, 'user_id': 1, 'category': 'groceries', 'limit': 500.0})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_investment(client):
	response = client.post('/investment', json={'id': 1, 'user_id': 1, 'value': 10000.0, 'roi': 0.05})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
