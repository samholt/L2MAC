import pytest
from models import User
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_view_profile(client):
	user = User('test_user', 'testemail', 'testpassword', [], [], [])
	app.users['test_user'] = user
	response = client.get('/view_profile', json={'username': 'test_user'})
	assert response.status_code == 200


def test_edit_profile(client):
	user = User('test_user', 'testemail', 'testpassword', [], [], [])
	app.users['test_user'] = user
	response = client.put('/edit_profile', json={'username': 'test_user', 'reading_interests': ['fiction', 'non-fiction']})
	assert response.status_code == 200


def test_follow_user(client):
	user1 = User('test_user', 'testemail', 'testpassword', [], [], [])
	user2 = User('another_user', 'anotheremail', 'anotherpassword', [], [], [])
	app.users['test_user'] = user1
	app.users['another_user'] = user2
	response = client.post('/follow_user', json={'username': 'test_user', 'user_to_follow': 'another_user'})
	assert response.status_code == 200


def test_unfollow_user(client):
	user1 = User('test_user', 'testemail', 'testpassword', [], [], [])
	user2 = User('another_user', 'anotheremail', 'anotherpassword', [], [], [])
	app.users['test_user'] = user1
	app.users['another_user'] = user2
	response = client.post('/unfollow_user', json={'username': 'test_user', 'user_to_unfollow': 'another_user'})
	assert response.status_code == 200
