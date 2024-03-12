import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client):
	response = client.post('/post', json={'user': 'test', 'post': 'Hello, World!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}


def test_get_posts(client):
	response = client.get('/posts')
	assert response.status_code == 200
	assert 'test' in response.get_json()
	assert response.get_json()['test'] == 'Hello, World!'


def test_post_without_content(client):
	response = client.post('/post', json={'user': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'No post content provided'}
