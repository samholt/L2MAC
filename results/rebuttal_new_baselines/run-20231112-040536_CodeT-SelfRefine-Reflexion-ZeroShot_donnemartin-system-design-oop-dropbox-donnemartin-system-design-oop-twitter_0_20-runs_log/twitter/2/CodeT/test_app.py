import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return {'username': 'test', 'email': 'test@test.com', 'password': 'test'}

@pytest.fixture
def sample_post():
	return {'user_id': 1, 'content': 'Hello, world!'}

@pytest.fixture
def sample_like():
	return {'post_id': 1}

@pytest.fixture
def sample_retweet():
	return {'post_id': 1}

@pytest.fixture
def sample_reply():
	return {'post_id': 1, 'reply': 'Nice post!'}


def test_register(client, sample_user):
	response = client.post('/register', json=sample_user)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client, sample_user):
	client.post('/register', json=sample_user)
	response = client.post('/login', json=sample_user)
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client, sample_user, sample_post):
	client.post('/register', json=sample_user)
	response = client.post('/post', json=sample_post)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Post created successfully'


def test_like(client, sample_user, sample_post, sample_like):
	client.post('/register', json=sample_user)
	client.post('/post', json=sample_post)
	response = client.post('/like', json=sample_like)
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post liked'


def test_retweet(client, sample_user, sample_post, sample_retweet):
	client.post('/register', json=sample_user)
	client.post('/post', json=sample_post)
	response = client.post('/retweet', json=sample_retweet)
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post retweeted'


def test_reply(client, sample_user, sample_post, sample_reply):
	client.post('/register', json=sample_user)
	client.post('/post', json=sample_post)
	response = client.post('/reply', json=sample_reply)
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Reply posted'
