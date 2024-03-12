import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users

	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

def test_login():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = response.get_json()
	assert 'token' in data
	decoded = jwt.decode(data['token'], app.SECRET_KEY, algorithms=['HS256'])
	assert decoded['user'] == 'test'

	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	token = jwt.encode({'user': 'test', 'exp': 9999999999}, app.SECRET_KEY, algorithm='HS256')
	response = app.app.test_client().post('/post', json={'token': token, 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}
	assert len(app.posts) == 1
	assert app.posts[0].content == 'Hello, world!'

	response = app.app.test_client().post('/post', json={'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is missing'}

	response = app.app.test_client().post('/post', json={'token': 'invalid', 'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is invalid'}
