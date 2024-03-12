import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'profile_picture': None, 'bio': None, 'website_link': None, 'location': None, 'is_private': False}


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'profile_picture': None, 'bio': None, 'website_link': None, 'location': None, 'is_private': False}


def test_post(client):
	response = client.post('/post', json={'id': '1', 'user_id': '1', 'content': 'Hello, world!', 'image': None})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'user_id': '1', 'content': 'Hello, world!', 'image': None}


def test_comment(client):
	response = client.post('/comment', json={'id': '1', 'post_id': '1', 'user_id': '1', 'content': 'Nice post!'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'post_id': '1', 'user_id': '1', 'content': 'Nice post!'}


def test_like(client):
	response = client.post('/like', json={'id': '1', 'post_id': '1', 'user_id': '1'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'post_id': '1', 'user_id': '1'}
