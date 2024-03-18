import pytest
from flask import json
from models.user import User
from routes.user import app, users_db, reset_tokens


def test_password_reset():
	# Register a user
	user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
	response = app.test_client().post('/register', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 201
	assert users_db['testuser'].username == 'testuser'
	assert users_db['testuser'].email == 'testuser@example.com'
	# Request password reset
	response = app.test_client().post('/password_reset_request', data=json.dumps({'email': 'testuser@example.com'}), content_type='application/json')
	assert response.status_code == 200
	# Get the reset token
	token = list(reset_tokens.keys())[0]
	# Reset password
	response = app.test_client().post('/password_reset', data=json.dumps({'token': token, 'new_password': 'newpassword'}), content_type='application/json')
	assert response.status_code == 200
	# Check the new password
	assert users_db['testuser'].check_password('newpassword')
	# Check that the token has been removed
	assert token not in reset_tokens
