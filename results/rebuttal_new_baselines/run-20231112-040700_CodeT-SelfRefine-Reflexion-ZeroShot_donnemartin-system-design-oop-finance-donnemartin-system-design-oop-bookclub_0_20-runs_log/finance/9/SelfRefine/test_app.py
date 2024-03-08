import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return {'id': '1', 'username': 'test', 'password': 'test'}

@pytest.fixture
def transaction():
	return {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False}


def test_create_user(client, user):
	response = client.post('/create_user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == user


def test_add_transaction(client, transaction):
	response = client.post('/add_transaction', data=json.dumps(transaction), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == transaction
