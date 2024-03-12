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
	user = User(email='test@test.com', username='test', password='test')
	response = client.post('/register', json=user.to_dict())
	assert response.status_code == 201
	assert response.get_json() == user.to_dict()


def test_login(client):
	user = User(email='test@test.com', username='test', password='test')
	app.users[user.email] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()


def test_create_post(client):
	post = Post(user_email='test@test.com', content='Hello, world!')
	response = client.post('/post', json=post.to_dict())
	assert response.status_code == 201
	assert response.get_json() == post.to_dict()


def test_get_post(client):
	post = Post(user_email='test@test.com', content='Hello, world!')
	app.posts[post.id] = post
	response = client.get(f'/post/{post.id}')
	assert response.status_code == 200
	assert response.get_json() == post.to_dict()
