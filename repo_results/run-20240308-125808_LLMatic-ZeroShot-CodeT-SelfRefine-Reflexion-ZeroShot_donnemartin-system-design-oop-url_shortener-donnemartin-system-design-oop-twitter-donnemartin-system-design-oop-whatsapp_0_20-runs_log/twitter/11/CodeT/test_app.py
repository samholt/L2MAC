import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return {'username': 'test', 'email': 'test@test.com', 'password': 'test'}

@pytest.fixture
def post():
	return {'user_id': 0, 'content': 'Hello, world!'}

@pytest.fixture
def token():
	return jwt.encode({'user_id': 0}, 'secret', algorithm='HS256')


def test_register(client, user):
	response = client.post('/register', json=user)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client, user):
	client.post('/register', json=user)
	response = client.post('/login', json=user)
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client, user, post, token):
	client.post('/register', json=user)
	response = client.post('/post', json=post, headers={'Authorization': f'Bearer {token}'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}
