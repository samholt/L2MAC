import pytest
import app
import jwt
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_update_profile(client):
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.put('/profile', json={'token': token, 'profile': {'bio': 'test bio'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}

	assert app.users['test']['profile'] == {'bio': 'test bio'}

def test_create_post(client):
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.post('/post', json={'token': token, 'text': 'test post'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

	assert len(app.posts) == 1
	assert app.posts[0]['text'] == 'test post'

def test_delete_post(client):
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = client.delete('/post/0', json={'token': token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}

	assert len(app.posts) == 0
