import pytest
from models import User, Post
from app import app
from database import users, posts

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_follow_unfollow(client):
	user1 = User('user1@test.com', 'user1', 'password')
	user2 = User('user2@test.com', 'user2', 'password')
	users['user1@test.com'] = user1
	users['user2@test.com'] = user2

	response = client.post('/follow', json={'email': 'user1@test.com', 'to_follow': 'user2@test.com'})
	assert response.get_json() == {'message': 'Followed successfully'}
	assert user2 in user1.following
	assert user1 in user2.followers

	response = client.post('/unfollow', json={'email': 'user1@test.com', 'to_unfollow': 'user2@test.com'})
	assert response.get_json() == {'message': 'Unfollowed successfully'}
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_get_following_posts(client):
	user1 = User('user1@test.com', 'user1', 'password')
	user2 = User('user2@test.com', 'user2', 'password')
	users['user1@test.com'] = user1
	users['user2@test.com'] = user2

	user1.follow(user2)
	post = Post(user2, 'Hello world!')
	user2.posts.append(post)

	response = client.get('/following_posts', json={'email': 'user1@test.com'})
	assert response.get_json() == {'posts': ['Hello world!']}
