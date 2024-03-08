import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created'}


def test_get_user(client):
	client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.get('/user/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'username': 'test', 'email': 'test@test.com'}


def test_create_transaction(client):
	client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	client.post('/user/test/account', json={'account_number': '123456', 'bank_name': 'Test Bank'})
	response = client.post('/user/test/transaction', json={'amount': 100, 'category': 'Test', 'date': '2022-01-01', 'is_recurring': False, 'is_deposit': True})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Transaction created'}


def test_create_account(client):
	client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/user/test/account', json={'account_number': '123456', 'bank_name': 'Test Bank'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Account created'}


def test_create_investment(client):
	client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/user/test/investment', json={'investment_name': 'Test Investment', 'investment_type': 'Stock', 'amount_invested': 1000})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Investment created'}
