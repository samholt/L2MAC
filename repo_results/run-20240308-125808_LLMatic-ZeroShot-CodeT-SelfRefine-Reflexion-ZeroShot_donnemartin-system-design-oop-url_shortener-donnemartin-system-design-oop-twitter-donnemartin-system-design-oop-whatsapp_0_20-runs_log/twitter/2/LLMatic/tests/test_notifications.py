import pytest
import json
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_notifications(client):
	# Register two users
	client.post('/register', json={'email': 'user1@example.com', 'username': 'user1', 'password': 'password'})
	client.post('/register', json={'email': 'user2@example.com', 'username': 'user2', 'password': 'password'})

	# User1 creates a post mentioning User2
	client.post('/post', json={'email': 'user1@example.com', 'content': 'Hello @user2', 'images': [], 'mentions': ['user2']})

	# User2 checks notifications and should have one notification
	response = client.get('/notifications', json={'email': 'user2@example.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert len(data['notifications']) == 1
	assert 'user1' in data['notifications'][0]
