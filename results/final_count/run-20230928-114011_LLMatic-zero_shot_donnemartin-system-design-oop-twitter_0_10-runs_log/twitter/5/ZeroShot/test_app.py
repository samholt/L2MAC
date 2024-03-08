import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.register()
	assert response.status_code == 200
	assert 'User registered successfully' in response.get_data(as_text=True)

	response = app.register()
	assert response.status_code == 400
	assert 'User already exists' in response.get_data(as_text=True)

	app.users = {}


def test_login():
	app.users = {'test': {'password': 'test'}}
	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_data(as_text=True)

	response = app.login()
	assert response.status_code == 400
	assert 'Invalid username or password' in response.get_data(as_text=True)

	app.users = {}
