import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users

def test_login():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()
	assert jwt.decode(response.get_json()['token'], app.SECRET_KEY, algorithms=['HS256'])['user'] == 'test'

	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = app.app.test_client().post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	app.posts = {}
	response = app.app.test_client().post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}
	assert len(app.posts) == 1

	response = app.app.test_client().post('/post', json={'username': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
