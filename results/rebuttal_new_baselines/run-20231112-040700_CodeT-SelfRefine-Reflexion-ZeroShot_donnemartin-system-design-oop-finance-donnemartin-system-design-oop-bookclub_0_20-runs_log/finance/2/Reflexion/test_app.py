import pytest
import app
from app import User, Account, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/users', json={'id': '1', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

	user = app.users['1']
	assert user.id == '1'
	assert user.email == 'test@example.com'
	assert user.password == 'password'

def test_create_account(client):
	app.users['1'] = User(id='1', email='test@example.com', password='password')

	response = client.post('/users/1/accounts', json={'id': '1', 'balance': 100.0})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

	account = app.accounts['1']
	assert account.id == '1'
	assert account.user_id == '1'
	assert account.balance == 100.0

def test_get_accounts(client):
	app.users['1'] = User(id='1', email='test@example.com', password='password')
	app.accounts['1'] = Account(id='1', user_id='1', balance=100.0)

	response = client.get('/users/1/accounts')
	assert response.status_code == 200
	assert response.get_json() == {'accounts': [{'id': '1', 'user_id': '1', 'balance': 100.0}]}

def test_create_transaction(client):
	app.accounts['1'] = Account(id='1', user_id='1', balance=100.0)

	response = client.post('/accounts/1/transactions', json={'id': '1', 'amount': 50.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

	transaction = app.transactions['1']
	assert transaction.id == '1'
	assert transaction.account_id == '1'
	assert transaction.amount == 50.0
	assert transaction.category == 'groceries'

def test_get_transactions(client):
	app.accounts['1'] = Account(id='1', user_id='1', balance=100.0)
	app.transactions['1'] = Transaction(id='1', account_id='1', amount=50.0, category='groceries')

	response = client.get('/accounts/1/transactions')
	assert response.status_code == 200
	assert response.get_json() == {'transactions': [{'id': '1', 'account_id': '1', 'amount': 50.0, 'category': 'groceries'}]}
