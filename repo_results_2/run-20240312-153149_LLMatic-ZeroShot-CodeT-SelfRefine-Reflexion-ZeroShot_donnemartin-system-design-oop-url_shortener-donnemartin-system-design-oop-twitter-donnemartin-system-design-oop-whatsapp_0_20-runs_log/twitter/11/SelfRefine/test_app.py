import pytest
import app
import jwt
import datetime

def test_register():
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users

	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

def test_login():
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()
	data = jwt.decode(response.get_json()['token'], app.SECRET_KEY, algorithms=['HS256'])
	assert data['user'] == 'test'

	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = app.app.test_client().post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post():
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.SECRET_KEY, algorithm='HS256')
	response = app.app.test_client().post('/post', json={'token': token, 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}
	assert len(app.posts) == 1
	assert app.posts[0].content == 'Hello, world!'

	response = app.app.test_client().post('/post', json={'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is missing'}

	response = app.app.test_client().post('/post', json={'token': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is invalid'}
