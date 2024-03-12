import pytest
from views import app
from models import User, Post

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_search(client):
	# Register a user
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200

	# Create a post
	response = client.post('/post', json={'email': 'test@test.com', 'content': 'Hello, World!', 'images': [], 'hashtags': ['test'], 'mentions': ['test']})
	assert response.status_code == 200

	# Search for the user
	response = client.get('/search', json={'keyword': 'test'})
	assert response.status_code == 200
	data = response.get_json()
	assert 'users' in data
	assert 'posts' in data
	assert len(data['users']) == 1
	assert len(data['posts']) == 1
	assert data['users'][0]['email'] == 'test@test.com'
	assert data['users'][0]['username'] == 'test'
	assert data['posts'][0]['content'] == 'Hello, World!'
	assert data['posts'][0]['hashtags'] == ['test']
	assert data['posts'][0]['mentions'] == ['test']
