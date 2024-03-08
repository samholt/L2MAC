import pytest
import app
from app import User, Transaction, Budget, Investment

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert app.users['1'].username == 'test'


def test_login(client):
	app.users['1'] = User(id='1', username='test', password='test')
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200


def test_add_transaction(client):
	response = client.post('/transactions', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False})
	assert response.status_code == 201
	assert app.transactions['1'].amount == 100.0


def test_add_budget(client):
	response = client.post('/budgets', json={'id': '1', 'user_id': '1', 'category': 'groceries', 'amount': 500.0})
	assert response.status_code == 201
	assert app.budgets['1'].amount == 500.0


def test_add_investment(client):
	response = client.post('/investments', json={'id': '1', 'user_id': '1', 'value': 1000.0, 'roi': 0.1})
	assert response.status_code == 201
	assert app.investments['1'].value == 1000.0
