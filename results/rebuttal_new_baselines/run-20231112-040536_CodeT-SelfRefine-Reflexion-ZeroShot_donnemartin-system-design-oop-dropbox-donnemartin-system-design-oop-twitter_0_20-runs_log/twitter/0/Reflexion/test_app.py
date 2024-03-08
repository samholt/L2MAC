import pytest
from app import app, users
from models import User

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 201
	assert 'User registered successfully' in response.get_data(as_text=True)
	assert len(users) == 1

def test_login(client):
	user = User(username='test', email='test@example.com', password_hash='', bio='', location='', website='', is_private=False)
	user.set_password('test')
	users[user.id] = user
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'Logged in successfully' in response.get_data(as_text=True)

def test_logout(client):
	response = client.get('/logout')
	assert response.status_code == 200
	assert 'Logged out successfully' in response.get_data(as_text=True)

def test_profile(client):
	user = User(username='test', email='test@example.com', password_hash='', bio='', location='', website='', is_private=False)
	user.set_password('test')
	users[user.id] = user
	response = client.get('/profile')
	assert response.status_code == 200
	assert 'test' in response.get_data(as_text=True)
