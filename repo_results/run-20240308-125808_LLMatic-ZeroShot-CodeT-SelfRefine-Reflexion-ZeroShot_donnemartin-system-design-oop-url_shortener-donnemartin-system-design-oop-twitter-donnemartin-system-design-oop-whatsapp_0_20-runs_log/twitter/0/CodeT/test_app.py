import pytest
import app
from user import User
from post import Post

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()

def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()

def test_create_post(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/posts', json={'user_email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 201
	post = response.get_json()
	assert post['user_email'] == 'test@test.com'
	assert post['content'] == 'Hello, world!'
