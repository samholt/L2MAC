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
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': '', 'website': '', 'location': '', 'private': False}


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': '', 'website': '', 'location': '', 'private': False}


def test_get_user(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.get('/users/test@test.com')
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': '', 'website': '', 'location': '', 'private': False}


def test_update_user(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.put('/users/test@test.com', json={'bio': 'Updated bio'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': 'Updated bio', 'website': '', 'location': '', 'private': False}


def test_create_post(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/posts', json={'user_email': 'test@test.com', 'content': 'Test post'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert 'created_at' in response.get_json()
	assert response.get_json()['user_email'] == 'test@test.com'
	assert response.get_json()['content'] == 'Test post'


def test_get_post(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/posts', json={'user_email': 'test@test.com', 'content': 'Test post'})
	post_id = response.get_json()['id']
	response = client.get(f'/posts/{post_id}')
	assert response.status_code == 200
	assert response.get_json()['id'] == post_id


def test_delete_post(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	response = client.post('/posts', json={'user_email': 'test@test.com', 'content': 'Test post'})
	post_id = response.get_json()['id']
	response = client.delete(f'/posts/{post_id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted'}
