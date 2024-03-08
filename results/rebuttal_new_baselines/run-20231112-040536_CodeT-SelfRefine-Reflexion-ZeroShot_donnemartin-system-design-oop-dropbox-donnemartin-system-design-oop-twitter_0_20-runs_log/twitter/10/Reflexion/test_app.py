import pytest
from app import app, User, database

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert database['test'] == User('test@test.com', 'test', 'test')

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

def test_profile(client):
	response = client.get('/profile', headers={'Authorization': 'Bearer ' + response.json['access_token']})
	assert response.status_code == 200
	assert response.json == {'email': 'test@test.com', 'username': 'test', 'password': 'test'}
