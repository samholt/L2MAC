import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'username': 'test', 'password': 'test'},
	{'id': '2', 'username': 'test2', 'password': 'test2'}
])
def test_create_user(client, user):
	response = client.post('/create_user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == user

@pytest.mark.parametrize('transaction', [
	{'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False},
	{'id': '2', 'user_id': '2', 'amount': 200.0, 'category': 'salary', 'recurring': True}
])
def test_add_transaction(client, transaction):
	response = client.post('/add_transaction', data=json.dumps(transaction), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == transaction
