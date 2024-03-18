import pytest
import app
import jwt

def test_register():
	response = app.register()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}

	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = app.post()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}

	response = app.login()
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = app.post()
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is missing'}

	response = app.post()
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is invalid'}
