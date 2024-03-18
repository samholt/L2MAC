import pytest
import app
import jwt
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'SECRET_KEY')
	return token

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Username already exists'

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid username or password'

def test_post(client, token):
	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!', 'token': token})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post created'

	response = client.post('/post', json={'user': 'test', 'content': 'This is a very long post that is definitely more than 280 characters. This is a very long post that is definitely more than 280 characters. This is a very long post that is definitely more than 280 characters. This is a very long post that is definitely more than 280 characters.', 'token': token})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Content too long'

def test_get_posts(client):
	response = client.get('/posts')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)
