import pytest
from models import User, Post, users_db, posts_db
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def setup():
	users_db.clear()
	posts_db.clear()
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	users_db[user1.email] = user1
	users_db[user2.email] = user2
	post1 = Post(user1, 'Hello #world', [])
	post2 = Post(user2, 'Hello @user1', [])
	posts_db['1'] = post1
	posts_db['2'] = post2


def test_search(client, setup):
	response = client.get('/search?query=Hello')
	assert response.status_code == 200
	assert 'user1' in [user['username'] for user in response.get_json()['users']]
	assert 'Hello #world' in [post['text'] for post in response.get_json()['posts']]


def test_filter_hashtags(client, setup):
	response = client.get('/filter?type=hashtags&value=#world')
	assert response.status_code == 200
	assert 'Hello #world' in [post['text'] for post in response.get_json()['posts']]


def test_filter_user_mentions(client, setup):
	response = client.get('/filter?type=user_mentions&value=@user1')
	assert response.status_code == 200
	assert 'Hello @user1' in [post['text'] for post in response.get_json()['posts']]


def test_filter_trending_topics(client, setup):
	response = client.get('/filter?type=trending_topics&value=Hello')
	assert response.status_code == 200
	assert 'Hello #world' in [post['text'] for post in response.get_json()['posts']]
	assert 'Hello @user1' in [post['text'] for post in response.get_json()['posts']]


def test_invalid_filter_type(client, setup):
	response = client.get('/filter?type=invalid&value=value')
	assert response.status_code == 400

