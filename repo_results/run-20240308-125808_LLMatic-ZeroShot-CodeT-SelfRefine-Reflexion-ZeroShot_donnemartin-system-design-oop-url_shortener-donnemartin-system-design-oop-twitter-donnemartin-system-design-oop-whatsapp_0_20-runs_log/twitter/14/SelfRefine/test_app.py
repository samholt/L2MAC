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
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()

def test_user(client):
	response = client.get('/users/test@test.com')
	assert response.status_code == 200
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()

	response = client.put('/users/test@test.com', json={'bio': 'This is a test bio'})
	assert response.status_code == 200
	assert response.get_json() == User(email='test@test.com', username='test', password='test', bio='This is a test bio').to_dict()

def test_create_post(client):
	response = client.post('/posts', json={'user_email': 'test@test.com', 'content': 'This is a test post'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['content'] == 'This is a test post'

def test_post(client):
	response = client.get('/posts/1')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Post not found'}

	response = client.delete('/posts/1')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Post not found'}
