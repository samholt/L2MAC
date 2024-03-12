import pytest
import app
import jwt

from flask import json


def test_register():
	with app.app.test_request_context('/register', method='POST', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json'):
		response = app.register()
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User registered successfully'}

		response = app.register()
		assert response.status_code == 400
		assert response.get_json() == {'message': 'User already exists'}

		app.users = {}


def test_login():
	with app.app.test_request_context('/login', method='POST', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json'):
		response = app.login()
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid username or password'}

		app.register()
		response = app.login()
		assert response.status_code == 200
		assert 'token' in response.get_json()
		assert jwt.decode(response.get_json()['token'], app.app.config['SECRET_KEY'], algorithms=['HS256'])['user'] == 'test'

		app.users = {}


def test_post():
	with app.app.test_request_context('/post', method='POST', data=json.dumps({'user': 'test', 'text': 'Hello, World!'}), content_type='application/json'):
		response = app.post()
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid user'}

		app.register()
		response = app.post()
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid post'}

		response = app.post()
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Post created successfully'}

		app.users = {}
		app.posts = {}
