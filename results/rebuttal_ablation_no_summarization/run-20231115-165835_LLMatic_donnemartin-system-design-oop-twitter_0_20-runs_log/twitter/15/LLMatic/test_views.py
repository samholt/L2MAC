import pytest
from flask import Flask
import views

app = Flask(__name__)
app.register_blueprint(views.views)

@pytest.fixture

def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/register', json={'username': 'test2', 'email': 'test2@test.com', 'password': 'test2'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'


def test_profile(client):
	response = client.get('/profile/test')
	assert response.status_code == 200


def test_post(client):
	response = client.post('/post', json={'username': 'test', 'text': 'Hello, world!', 'image': ''})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post created'


def test_user_posts(client):
	response = client.get('/posts/test')
	assert response.status_code == 200


def test_follow(client):
	response = client.post('/follow', json={'username': 'test', 'follow_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Followed user'


def test_unfollow(client):
	response = client.post('/unfollow', json={'username': 'test', 'unfollow_username': 'test2'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Unfollowed user'
