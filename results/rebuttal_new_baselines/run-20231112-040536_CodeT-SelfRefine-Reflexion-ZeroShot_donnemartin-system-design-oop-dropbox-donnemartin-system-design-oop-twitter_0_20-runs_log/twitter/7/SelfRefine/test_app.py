import pytest
import app
import jwt
from flask import json

def test_register():
	with app.app.test_client() as c:
		app.users = {}
		response = c.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User registered successfully'}

		response = c.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Username already exists'}

		app.users = {}


def test_login():
	with app.app.test_client() as c:
		app.users = {'test': {'username': 'test', 'password': 'test'}}
		response = c.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'token' in response.get_json()

		response = c.post('/login', data=json.dumps({'username': 'test', 'password': 'wrong'}), content_type='application/json')
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid username or password'}

		app.users = {}


def test_post():
	with app.app.test_client() as c:
		app.users = {'test': {'username': 'test', 'password': 'test'}}
		app.posts = {}
		token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		response = c.post('/post', data=json.dumps({'token': token, 'post': 'Hello, World!'}), content_type='application/json')
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Post created'}

		response = c.post('/post', data=json.dumps({'token': 'invalid', 'post': 'Hello, World!'}), content_type='application/json')
		assert response.status_code == 401
		assert response.get_json() == {'message': 'Token is invalid'}

		app.users = {}
		app.posts = {}
