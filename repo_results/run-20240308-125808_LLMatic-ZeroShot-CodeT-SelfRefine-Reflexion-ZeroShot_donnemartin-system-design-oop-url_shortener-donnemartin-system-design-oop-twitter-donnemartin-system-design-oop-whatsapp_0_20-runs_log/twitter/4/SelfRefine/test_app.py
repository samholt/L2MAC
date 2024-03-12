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
	return jwt.encode({'user': 'test', 'exp': app.datetime.datetime.utcnow() + app.datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client, token):
	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}


def test_like(client, token):
	response = client.post('/like', json={'post_id': 0}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Liked successfully'}


def test_retweet(client, token):
	response = client.post('/retweet', json={'post_id': 0}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Retweeted successfully'}


def test_reply(client, token):
	response = client.post('/reply', json={'post_id': 0, 'reply': 'Hello, test!'}, headers={'Authorization': 'Bearer ' + token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Replied successfully'}
