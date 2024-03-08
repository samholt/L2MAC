import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {'users': {}, 'accounts': {}, 'transactions': {}}

@pytest.mark.usefixtures('reset_db')
def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'id': '1', 'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['users']['1'].username == 'test'

@pytest.mark.usefixtures('reset_db')
def test_create_account(client):
	response = client.post('/create_account', data=json.dumps({'id': '1', 'user_id': '1', 'balance': 1000.0}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['accounts']['1'].balance == 1000.0

@pytest.mark.usefixtures('reset_db')
def test_create_transaction(client):
	response = client.post('/create_transaction', data=json.dumps({'id': '1', 'account_id': '1', 'amount': 100.0, 'category': 'groceries'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['transactions']['1'].amount == 100.0
