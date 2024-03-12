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
	user = User(email='test@test.com', username='test', password='test')
	app.users[user.email] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test', 'bio': '', 'website': '', 'location': '', 'private': False}


def test_create_post(client):
	response = client.post('/post', json={'user_email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 201
	json = response.get_json()
	assert json['user_email'] == 'test@test.com'
	assert json['content'] == 'Hello, world!'


def test_get_post(client):
	post = Post(user_email='test@test.com', content='Hello, world!')
	app.posts[post.id] = post
	response = client.get(f'/post/{post.id}')
	assert response.status_code == 200
	json = response.get_json()
	assert json['id'] == post.id
	assert json['user_email'] == 'test@test.com'
	assert json['content'] == 'Hello, world!'
