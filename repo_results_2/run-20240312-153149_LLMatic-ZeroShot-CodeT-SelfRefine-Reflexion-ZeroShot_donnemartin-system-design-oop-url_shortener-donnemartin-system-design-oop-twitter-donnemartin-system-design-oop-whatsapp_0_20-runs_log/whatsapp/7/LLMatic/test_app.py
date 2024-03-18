import pytest
from app import app, users, statuses
import datetime

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

# Test user registration
@pytest.mark.parametrize(('username', 'message'), (
	('user1', b'User registered successfully'),
	('user1', b'Username already exists'),
))
def test_register(client, username, message):
	response = client.post('/register', json={'username': username})
	assert message in response.data

# Test add friend
@pytest.mark.parametrize(('username', 'friend_username', 'message'), (
	('user1', 'user2', b'User not found'),
	('user1', 'user1', b'Friend added successfully'),
))
def test_add_friend(client, username, friend_username, message):
	response = client.post('/add_friend', json={'username': username, 'friend_username': friend_username})
	assert message in response.data

# Test post status
@pytest.mark.parametrize(('username', 'image_url', 'visibility', 'message'), (
	('user1', 'http://example.com/image.jpg', 'public', b'Status posted successfully'),
	('user2', 'http://example.com/image.jpg', 'public', b'User not found'),
))
def test_post_status(client, username, image_url, visibility, message):
	response = client.post('/post_status', json={'username': username, 'image_url': image_url, 'visibility': visibility})
	assert message in response.data

# Test get statuses
def test_get_statuses(client):
	client.post('/register', json={'username': 'user2'})
	client.post('/add_friend', json={'username': 'user1', 'friend_username': 'user2'})
	client.post('/post_status', json={'username': 'user2', 'image_url': 'http://example.com/image.jpg', 'visibility': 'friends'})
	response = client.get('/get_statuses', query_string={'username': 'user1'})
	data = response.get_json()
	assert len(data['user_statuses']) == 1
	assert len(data['friend_statuses']) == 1
	assert (datetime.datetime.now() - datetime.datetime.fromisoformat(data['user_statuses'][0]['timestamp'])).total_seconds() <= 86400
	assert (datetime.datetime.now() - datetime.datetime.fromisoformat(data['friend_statuses'][0]['timestamp'])).total_seconds() <= 86400

# Test update status
def test_update_status(client):
	client.post('/register', json={'username': 'user2'})
	client.post('/add_friend', json={'username': 'user1', 'friend_username': 'user2'})
	client.post('/post_status', json={'username': 'user1', 'image_url': 'http://example.com/image.jpg', 'visibility': 'friends'})
	response = client.post('/update_status', json={'username': 'user2', 'online': True})
	data = response.get_json()
	assert b'User is now online' in response.data
	assert len(data['messages']) == 2
	assert 'user1 added you as a friend.' in data['messages']
	assert 'user1 posted a new status.' in data['messages']
	response = client.post('/update_status', json={'username': 'user2', 'online': False})
	assert b'User is now offline' in response.data

