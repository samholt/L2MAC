import pytest
import app
from app import User, Post

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert isinstance(app.users['test@example.com'], User)


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_update_profile(client):
	response = client.put('/update_profile', json={'name': 'Updated User', 'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}
	assert app.users['test@example.com'].name == 'Updated User'


def test_create_post(client):
	response = client.post('/create_post', json={'content': 'Test post', 'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}
	assert isinstance(app.posts[0], Post)
