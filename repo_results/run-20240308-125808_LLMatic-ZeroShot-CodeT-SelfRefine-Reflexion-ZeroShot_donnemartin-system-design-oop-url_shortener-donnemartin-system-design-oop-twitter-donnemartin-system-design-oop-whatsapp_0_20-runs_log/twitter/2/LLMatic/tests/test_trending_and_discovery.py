import pytest
from views import app
from models import User, Post

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_trending(client):
	response = client.get('/trending')
	assert response.status_code == 200


def test_recommend(client):
	user1 = User('user1@test.com', 'user1', 'password')
	user2 = User('user2@test.com', 'user2', 'password')
	user3 = User('user3@test.com', 'user3', 'password')
	user4 = User('user4@test.com', 'user4', 'password')
	user1.followers = ['user2@test.com', 'user3@test.com']
	user2.followers = ['user1@test.com', 'user3@test.com']
	user3.followers = ['user1@test.com', 'user2@test.com']
	user4.followers = ['user1@test.com', 'user2@test.com', 'user3@test.com']
	views.users = {'user1@test.com': user1, 'user2@test.com': user2, 'user3@test.com': user3, 'user4@test.com': user4}
	response = client.get('/recommend', json={'email': 'user1@test.com'})
	assert response.status_code == 200
	assert response.get_json() == [{'email': 'user4@test.com', 'username': 'user4', 'mutual_followers': 2}]
