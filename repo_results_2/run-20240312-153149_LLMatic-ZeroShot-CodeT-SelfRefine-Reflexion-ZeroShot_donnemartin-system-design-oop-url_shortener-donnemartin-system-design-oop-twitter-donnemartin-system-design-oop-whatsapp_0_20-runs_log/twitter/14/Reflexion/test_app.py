import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	return response.get_json()['id']

@pytest.fixture
def post(client, user):
	response = client.post('/posts', json={'user_id': user, 'content': 'Hello, world!'})
	return response.get_json()['id']

@pytest.fixture
def token(client, user):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	return response.get_json()['token']


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client, user):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_user(client, user):
	response = client.get(f'/users/{user}')
	assert response.status_code == 200
	data = response.get_json()
	assert data['username'] == 'test'
	assert data['email'] == 'test@test.com'


def test_create_post(client, user):
	response = client.post('/posts', json={'user_id': user, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_post(client, post):
	response = client.get(f'/posts/{post}')
	assert response.status_code == 200
	data = response.get_json()
	assert data['user_id'] == 0
	assert data['content'] == 'Hello, world!'


def test_follow(client, user):
	response = client.post('/follow', json={'follower_id': user, 'followee_id': user})
	assert response.status_code == 200


def test_unfollow(client, user):
	client.post('/follow', json={'follower_id': user, 'followee_id': user})
	response = client.post('/unfollow', json={'follower_id': user, 'followee_id': user})
	assert response.status_code == 200


def test_timeline(client, user, post):
	client.post('/follow', json={'follower_id': user, 'followee_id': user})
	response = client.get(f'/timeline/{user}')
	assert response.status_code == 200
	data = response.get_json()
	assert len(data) == 1
	assert data[0]['user_id'] == user
	assert data[0]['content'] == 'Hello, world!'
