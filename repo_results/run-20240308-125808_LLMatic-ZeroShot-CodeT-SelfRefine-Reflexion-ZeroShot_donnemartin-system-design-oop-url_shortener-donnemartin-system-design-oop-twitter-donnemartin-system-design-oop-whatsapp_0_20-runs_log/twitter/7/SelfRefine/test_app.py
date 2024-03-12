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
	return Post(user_email=user.email, content='Hello, world!')


def test_register(client, user):
	response = client.post('/register', json={'email': user.email, 'username': user.username, 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'email': user.email, 'username': user.username, 'bio': '', 'website': '', 'location': '', 'private': False}


def test_login(client, user):
	app.users[user.email] = user
	response = client.post('/login', json={'email': user.email, 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'email': user.email, 'username': user.username, 'bio': '', 'website': '', 'location': '', 'private': False}


def test_create_post(client, post):
	response = client.post('/posts', json=post.to_dict())
	assert response.status_code == 201
	assert response.get_json() == {'user_email': post.user_email, 'content': post.content, 'image_url': '', 'likes': 0, 'retweets': 0, 'replies': 0, 'id': post.id, 'created_at': post.created_at.strftime('%a, %d %b %Y %H:%M:%S GMT')}
