import pytest
from models import User, Post
from database import users, posts
from app import app as flask_app


@pytest.fixture
def app():
	return flask_app


def test_search_users(app):
	client = app.test_client()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	response = client.post('/search', json={'keyword': 'user1'})
	assert response.status_code == 200
	data = response.get_json()
	assert len(data['users']) == 1
	assert data['users'][0] == 'user1@example.com'


def test_search_posts(app):
	client = app.test_client()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	post1 = Post(user1, 'Hello world!')
	post2 = Post(user2, 'Hello again!')
	posts.extend([post1, post2])
	response = client.post('/search', json={'keyword': 'Hello'})
	assert response.status_code == 200
	data = response.get_json()
	assert len(data['posts']) == 2
	assert 'Hello world!' in data['posts']
	assert 'Hello again!' in data['posts']
