import pytest
import app
import jwt
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	return token


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_update_profile(client, token):
	response = client.put('/profile', json={'username': 'test', 'bio': 'test bio', 'website': 'test.com', 'location': 'test location'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}


def test_create_post(client, token):
	response = client.post('/post', json={'username': 'test', 'content': 'test content'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}


def test_delete_post(client, token):
	response = client.delete('/post', json={'username': 'test'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}


def test_follow_user(client, token):
	response = client.post('/follow', json={'username': 'test', 'follow_username': 'test2'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Followed user successfully'}


def test_unfollow_user(client, token):
	response = client.post('/unfollow', json={'username': 'test', 'unfollow_username': 'test2'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Unfollowed user successfully'}
