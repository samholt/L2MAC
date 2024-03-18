import pytest
from flask import json
from models.user import User
from routes.user import app, users_db, reset_tokens


def test_user_registration():
	# Register a user
	user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
	response = app.test_client().post('/register', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 201
	assert users_db['testuser'].username == 'testuser'
	assert users_db['testuser'].email == 'testuser@example.com'


def test_user_login():
	# Register a user
	user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
	response = app.test_client().post('/register', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 201
	# Login the user
	login_data = {'username': 'testuser', 'password': 'testpassword'}
	response = app.test_client().post('/login', data=json.dumps(login_data), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['token'] == 'testuser'


def test_password_reset():
	# Register a user
	user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
	response = app.test_client().post('/register', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 201
	# Request password reset
	reset_request_data = {'email': 'testuser@example.com'}
	response = app.test_client().post('/password_reset_request', data=json.dumps(reset_request_data), content_type='application/json')
	assert response.status_code == 200
	# Reset password
	reset_data = {'token': list(reset_tokens.keys())[0], 'new_password': 'newpassword'}
	response = app.test_client().post('/password_reset', data=json.dumps(reset_data), content_type='application/json')
	assert response.status_code == 200
	# Login with new password
	login_data = {'username': 'testuser', 'password': 'newpassword'}
	response = app.test_client().post('/login', data=json.dumps(login_data), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['token'] == 'testuser'
