import pytest
import app
from user import User
from post import Post

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
	return Post(user_email=user.email, content='Hello, World!')


def test_register(client, user):
	response = client.post('/register', json=user.to_dict())
	assert response.status_code == 201
	assert response.get_json() == user.to_dict()


def test_login(client, user):
	app.users[user.email] = user
	response = client.post('/login', json={'email': user.email, 'password': user.password})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()


def test_create_post(client, user, post):
	app.users[user.email] = user
	response = client.post('/posts', json=post.to_dict())
	assert response.status_code == 201
	assert response.get_json() == post.to_dict()


def test_get_post(client, post):
	app.posts[post.id] = post
	response = client.get(f'/posts/{post.id}')
	assert response.status_code == 200
	assert response.get_json() == post.to_dict()


def test_delete_post(client, post):
	app.posts[post.id] = post
	response = client.delete(f'/posts/{post.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted'}
