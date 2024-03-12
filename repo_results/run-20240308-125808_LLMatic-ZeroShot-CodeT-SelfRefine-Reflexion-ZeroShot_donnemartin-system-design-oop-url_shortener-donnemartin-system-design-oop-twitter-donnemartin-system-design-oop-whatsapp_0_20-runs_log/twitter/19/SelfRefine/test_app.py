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
	token = jwt.encode({'user': 'testuser', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	return token


def test_register(client):
	response = client.post('/register', json={'username': 'testuser', 'password': 'testpass'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client):
	response = client.post('/post', json={'user': 'testuser', 'content': 'testpost'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}


def test_get_posts(client):
	response = client.get('/posts/testuser')
	assert response.status_code == 200
	assert response.get_json() == {'posts': 'testpost'}
