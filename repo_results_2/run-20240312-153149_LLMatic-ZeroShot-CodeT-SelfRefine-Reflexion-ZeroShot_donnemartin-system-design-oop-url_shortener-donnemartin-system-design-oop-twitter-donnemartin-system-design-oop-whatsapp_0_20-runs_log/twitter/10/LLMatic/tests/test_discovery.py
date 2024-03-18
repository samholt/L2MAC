import pytest
from models import User, Post
from database import users, posts
from app import app as flask_app


@pytest.fixture
def app():
	return flask_app


def test_trending(app):
	client = app.test_client()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	post1 = Post(user1, 'content #topic1')
	post2 = Post(user2, 'content #topic1')
	post3 = Post(user1, 'content #topic2')
	posts.extend([post1, post2, post3])
	response = client.get('/trending')
	assert response.status_code == 200
	trending = response.get_json()['trending']
	assert len(trending) == 2
	assert '#topic1' in trending


def test_recommend(app):
	client = app.test_client()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	user3 = User('user3@example.com', 'user3', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	users[user3.email] = user3
	user1.follow(user2)
	user3.follow(user2)
	post1 = Post(user2, 'content #topic1')
	post2 = Post(user3, 'content #topic1')
	posts.extend([post1, post2])
	response = client.get('/recommend', json={'email': user1.email})
	assert response.status_code == 200
	recommendations = response.get_json()['recommendations']
	assert len(recommendations) == 2
	assert user3.email in recommendations
	assert 'test@example.com' in recommendations
