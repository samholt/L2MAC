import pytest
import app
import jwt
import hashlib

def test_register():
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users
	assert app.users['test'].password == hashlib.sha256('test'.encode()).hexdigest()

	response = app.app.test_client().post('/register', json={'username': '', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid input'}

	response = app.app.test_client().post('/register', json={'username': 'test', 'email': '', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid input'}

	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': ''})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid input'}

def test_login():
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
	response = app.app.test_client().post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}
	assert len(app.posts) == 1
	assert app.posts[0].user == 'test'
	assert app.posts[0].content == 'Hello, world!'

	response = app.app.test_client().post('/post', json={'username': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
