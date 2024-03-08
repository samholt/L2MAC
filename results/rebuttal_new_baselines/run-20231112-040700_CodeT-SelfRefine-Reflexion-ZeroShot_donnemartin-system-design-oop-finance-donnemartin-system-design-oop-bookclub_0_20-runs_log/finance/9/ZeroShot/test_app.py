import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_transaction(client):
	response = client.post('/create_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries', 'recurring': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction created successfully'}
