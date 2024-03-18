import pytest
import jwt
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
	user1 = User('user1@test.com', 'user1', 'password1')
	user2 = User('user2@test.com', 'user2', 'password2')
	user3 = User('user3@test.com', 'user3', 'password3')
	users_db['user1'] = user1
	users_db['user2'] = user2
	users_db['user3'] = user3
	post1 = Post('post1', user='user1')
	post2 = Post('post2', user='user2')
	post3 = Post('post3', user='user3')
	post1.likes = 10
	post2.likes = 20
	post3.likes = 30
	posts_db[1] = post1
	posts_db[2] = post2
	posts_db[3] = post3


def test_trending(client, setup):
	response = client.get('/trending')
	assert response.status_code == 200
	assert len(response.get_json()) == 3
	assert response.get_json()[0]['text'] == 'post3'


def test_recommendations(client, setup):
	response = client.get('/recommendations/user1')
	assert response.status_code == 200
	assert len(response.get_json()) == 2
	assert 'user3' in response.get_json()
	assert 'user2' in response.get_json()
	assert 'user1' not in response.get_json()

