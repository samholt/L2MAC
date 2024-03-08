import pytest
from app import app, users, bank_accounts, transactions

@pytest.fixture
def client():
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.data == b'Home Page'


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.data == b'User created successfully'
	assert 'test' in users


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.data == b'Login successful'
	with client.session_transaction() as session:
		assert 'username' in session


def test_invalid_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.data == b'Invalid username or password'


def test_add_bank_account(client):
	response = client.post('/add_bank_account', json={'username': 'test', 'bank_name': 'Test Bank', 'account_number': '123456', 'balance': 1000})
	assert response.data == b'Bank account added successfully'
	assert 'test' in bank_accounts
	assert bank_accounts['test'].balance == 1000


def test_update_balance(client):
	bank_accounts['test'].update_balance('test', 2000)
	assert bank_accounts['test'].balance == 2000


def test_add_transaction(client):
	response = client.post('/add_transaction', json={'username': 'test', 'amount': 100, 'category': 'Food', 'date': '2022-01-01'})
	assert response.data == b'Transaction added successfully'
	assert 'test' in transactions
	assert transactions['test'][0].amount == 100
	assert transactions['test'][0].category == 'Food'
	assert transactions['test'][0].date == '2022-01-01'

