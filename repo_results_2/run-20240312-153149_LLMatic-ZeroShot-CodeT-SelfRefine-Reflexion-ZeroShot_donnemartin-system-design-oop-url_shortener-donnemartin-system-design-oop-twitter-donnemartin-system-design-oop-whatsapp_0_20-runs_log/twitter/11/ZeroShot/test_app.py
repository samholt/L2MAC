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
	app.users['test@test.com'] = User('test@test.com', 'test', 'test')
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': '', 'website': '', 'location': '', 'private': False}


def test_create_post(client):
	response = client.post('/post', json={'user_email': 'test@test.com', 'content': 'Hello, world!'})
	json_data = response.get_json()
	assert response.status_code == 201
	assert 'id' in json_data
	assert json_data['user_email'] == 'test@test.com'
	assert json_data['content'] == 'Hello, world!'


def test_get_post(client):
	post = Post('test@test.com', 'Hello, world!')
	app.posts[post.id] = post
	response = client.get(f'/post/{post.id}')
	json_data = response.get_json()
	assert response.status_code == 200
	assert json_data['id'] == post.id
	assert json_data['user_email'] == 'test@test.com'
	assert json_data['content'] == 'Hello, world!'
