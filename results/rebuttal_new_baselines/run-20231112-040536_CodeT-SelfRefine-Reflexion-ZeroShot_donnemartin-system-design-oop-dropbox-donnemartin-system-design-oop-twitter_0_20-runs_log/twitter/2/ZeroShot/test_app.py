import pytest
import app
import jwt

def test_register():
	response = app.register()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}

	response = app.register()
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

def test_login():
	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = app.login()
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post():
	response = app.post()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}

	response = app.post()
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
