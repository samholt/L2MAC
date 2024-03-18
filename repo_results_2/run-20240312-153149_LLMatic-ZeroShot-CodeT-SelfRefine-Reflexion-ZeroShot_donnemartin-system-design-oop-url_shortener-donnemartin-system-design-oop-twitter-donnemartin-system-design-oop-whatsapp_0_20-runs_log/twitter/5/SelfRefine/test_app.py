import pytest
import app
import jwt
from flask import json


def test_register():
	with app.app.test_client() as client:
		response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200
		assert 'message' in response.get_json()
		assert response.get_json()['message'] == 'Registered successfully'

		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'token' in response.get_json()

		token = response.get_json()['token']
		data = jwt.decode(token, app.SECRET_KEY)
		assert 'user' in data
		assert 'exp' in data

		response = client.post('/post', json={'token': token, 'user': 'test', 'content': 'Hello, World!'})
		assert response.status_code == 200
		assert 'message' in response.get_json()
		assert response.get_json()['message'] == 'Posted successfully'

		assert len(app.posts) == 1
