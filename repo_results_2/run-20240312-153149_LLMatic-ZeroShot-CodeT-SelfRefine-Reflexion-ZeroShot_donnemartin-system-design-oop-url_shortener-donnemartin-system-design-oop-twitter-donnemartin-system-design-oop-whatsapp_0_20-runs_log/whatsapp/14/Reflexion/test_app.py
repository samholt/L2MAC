import pytest
import app
from app import User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'email': 'test@test.com'}


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	json_data = response.get_json()
	assert response.status_code == 200
	assert json_data['email'] == 'test@test.com'
