import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	return jwt.encode({'user_id': 0}, 'secret', algorithm='HS256')

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

def test_post(client, token):
	response = client.post('/post', json={'token': token, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}

def test_like(client, token):
	response = client.post('/like', json={'token': token, 'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post liked'}

def test_retweet(client, token):
	response = client.post('/retweet', json={'token': token, 'post_id': 0})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post retweeted'}

def test_reply(client, token):
	response = client.post('/reply', json={'token': token, 'post_id': 0, 'reply': 'Nice post!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Reply posted'}

def test_get_posts(client):
	response = client.get('/posts')
	assert response.status_code == 200
	assert 'posts' in response.get_json()
