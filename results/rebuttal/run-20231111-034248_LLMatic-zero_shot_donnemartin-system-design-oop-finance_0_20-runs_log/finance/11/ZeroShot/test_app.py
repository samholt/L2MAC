import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'username': 'test', 'password': 'test'}


def test_login(client):
	client.post('/register', json={'id': '1', 'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'username': 'test', 'password': 'test'}


def test_add_transaction(client):
	response = client.post('/transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'}
