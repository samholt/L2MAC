import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	return jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY']).decode('UTF-8')


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client, token):
	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!', 'token': token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created'}
