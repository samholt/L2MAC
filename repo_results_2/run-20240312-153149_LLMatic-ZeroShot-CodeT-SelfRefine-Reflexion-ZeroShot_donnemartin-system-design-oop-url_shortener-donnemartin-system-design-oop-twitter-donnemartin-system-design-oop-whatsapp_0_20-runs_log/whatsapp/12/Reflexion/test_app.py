import pytest
import app
import uuid

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	user_id = response.get_json()['id']
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged In', 'id': user_id}
