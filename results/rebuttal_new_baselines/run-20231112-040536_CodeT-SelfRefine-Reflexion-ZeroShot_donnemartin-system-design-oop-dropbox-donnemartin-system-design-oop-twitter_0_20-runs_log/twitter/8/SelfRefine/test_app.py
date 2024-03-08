import pytest
import app
import jwt
from werkzeug.security import generate_password_hash

def test_register():
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users
	assert app.users['test'].password != 'test'

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

def test_update_post():
	response = app.app.test_client().put('/post/0', json={'username': 'test', 'content': 'Updated content'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post updated successfully'}
	assert app.posts[0].content == 'Updated content'

	response = app.app.test_client().put('/post/0', json={'username': 'wrong', 'content': 'Updated content'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Post not found or unauthorized'}

def test_delete_post():
	response = app.app.test_client().delete('/post/0', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}
	assert len(app.posts) == 0

	response = app.app.test_client().delete('/post/0', json={'username': 'wrong'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Post not found or unauthorized'}
