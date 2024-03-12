import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_profile(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.get('/profile', headers={'Authorization': token})
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'


def test_post(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.post('/post', headers={'Authorization': token}, json={'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}


def test_follow(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.post('/follow', headers={'Authorization': token}, json={'username': 'test2'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found or already followed'}


def test_unfollow(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.post('/unfollow', headers={'Authorization': token}, json={'username': 'test2'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found or not followed'}


def test_timeline(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.get('/timeline', headers={'Authorization': token})
	assert response.status_code == 200
	assert 'posts' in response.get_json()


def test_search(client):
	response = client.get('/search', query_string={'q': 'test'})
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'posts' in response.get_json()


def test_filter(client):
	response = client.get('/filter', query_string={'hashtags': ['test'], 'mentions': ['test'], 'trending': 'test'})
	assert response.status_code == 200
	assert 'posts' in response.get_json()


def test_message(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.post('/message', headers={'Authorization': token}, json={'content': 'Hello, test2', 'recipient': 'test2'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Message sent successfully'}


def test_notifications(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.get('/notifications', headers={'Authorization': token})
	assert response.status_code == 200
	assert 'notifications' in response.get_json()


def test_trending(client):
	response = client.get('/trending')
	assert response.status_code == 200
	assert 'trending' in response.get_json()


def test_recommendations(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.get('/recommendations', headers={'Authorization': token})
	assert response.status_code == 200
	assert 'recommendations' in response.get_json()

