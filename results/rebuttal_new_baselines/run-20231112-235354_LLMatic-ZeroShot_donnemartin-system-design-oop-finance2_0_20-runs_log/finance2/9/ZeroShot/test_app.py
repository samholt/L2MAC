import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'username': 'test', 'password': 'test'},
])
def test_create_user(client, user):
	response = client.post('/create_user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE[user['id']] == app.User(**user)

@pytest.mark.parametrize('account', [
	{'id': '1', 'user_id': '1', 'balance': 1000.0},
])
def test_create_account(client, account):
	response = client.post('/create_account', data=json.dumps(account), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE[account['id']] == app.Account(**account)

@pytest.mark.parametrize('transaction', [
	{'id': '1', 'account_id': '1', 'amount': 100.0, 'category': 'groceries'},
])
def test_create_transaction(client, transaction):
	response = client.post('/create_transaction', data=json.dumps(transaction), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE[transaction['id']] == app.Transaction(**transaction)
