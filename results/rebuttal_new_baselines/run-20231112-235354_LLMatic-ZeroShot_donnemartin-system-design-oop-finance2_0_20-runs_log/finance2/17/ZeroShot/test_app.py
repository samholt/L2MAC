import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_data():
	return {
		'id': '1',
		'username': 'test',
		'password': 'test'
	}

@pytest.fixture
def sample_account():
	return {
		'id': '1',
		'user_id': '1',
		'balance': 1000.0
	}

@pytest.fixture
def sample_transaction():
	return {
		'id': '1',
		'account_id': '1',
		'amount': 200.0,
		'category': 'groceries'
	}


def test_create_user(client, sample_data):
	response = client.post('/create_user', data=json.dumps(sample_data), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['users']['1'].username == 'test'


def test_create_account(client, sample_account):
	response = client.post('/create_account', data=json.dumps(sample_account), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['accounts']['1'].balance == 1000.0


def test_create_transaction(client, sample_transaction):
	response = client.post('/create_transaction', data=json.dumps(sample_transaction), content_type='application/json')
	assert response.status_code == 200
	assert app.DB['transactions']['1'].amount == 200.0
