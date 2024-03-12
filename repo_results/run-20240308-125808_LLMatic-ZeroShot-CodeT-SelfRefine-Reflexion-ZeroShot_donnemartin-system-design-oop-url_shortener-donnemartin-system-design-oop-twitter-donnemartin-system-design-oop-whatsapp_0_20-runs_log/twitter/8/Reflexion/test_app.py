import pytest
import app
from user import User
from post import Post
from datetime import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User(email='test@test.com', username='test', password='test')

@pytest.fixture
def post(user):
	return Post(id='1', user_email=user.email, content='Hello, world!')


def test_register(client, user):
	response = client.post('/register', json=user.to_dict())
	assert response.status_code == 201
	assert response.get_json() == user.to_dict()


def test_login(client, user):
	app.users[user.email] = user
	response = client.post('/login', json={'email': user.email, 'password': user.password})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()


def test_get_user(client, user):
	app.users[user.email] = user
	response = client.get(f'/users/{user.email}')
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()


def test_update_user(client, user):
	app.users[user.email] = user
	response = client.put(f'/users/{user.email}', json={'bio': 'Hello, world!'})
	assert response.status_code == 200
	user.bio = 'Hello, world!'
	assert response.get_json() == user.to_dict()


def test_create_post(client, post):
	response = client.post('/posts', json=post.to_dict())
	assert response.status_code == 201
	assert response.get_json() == post.to_dict()


def test_get_post(client, post):
	app.posts[post.id] = post
	response = client.get(f'/posts/{post.id}')
	assert response.status_code == 200
	assert response.get_json() == {**post.to_dict(), 'created_at': post.created_at.strftime('%Y-%m-%dT%H:%M:%S')}
