import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'password' not in json.loads(response.data)


def test_create_transaction(client):
	response = client.post('/create_transaction', json={'id': '1', 'user_id': '1', 'password': 'test', 'amount': 100.0, 'category': 'groceries', 'recurring': False})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False}
