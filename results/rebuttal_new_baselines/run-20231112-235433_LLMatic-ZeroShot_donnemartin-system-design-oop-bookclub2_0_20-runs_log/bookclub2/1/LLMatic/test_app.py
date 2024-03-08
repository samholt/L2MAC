import pytest
import app
from models import User
from flask import request

# Rest of the file remains the same

def test_view_profile():
	user = User('testuser', 'testuser@example.com', 'password_hash')
	app.users['testuser'] = user
	with app.app.test_request_context(json={'username': 'testuser'}):
		response = app.view_profile()
	assert response[0] == {'username': 'testuser', 'email': 'testuser@example.com', 'first_name': '', 'last_name': '', 'bio': '', 'profile_picture': ''}
	assert response[1] == 200


def test_edit_profile():
	user = User('testuser', 'testuser@example.com', 'password_hash')
	app.users['testuser'] = user
	with app.app.test_request_context(json={'username': 'testuser', 'first_name': 'Updated', 'last_name': 'User', 'bio': 'This is an updated test user.', 'profile_picture': 'updated_profile_picture.jpg'}):
		response = app.edit_profile()
	assert response[0] == {'message': 'Profile updated successfully'}
	assert response[1] == 200
	assert user.first_name == 'Updated'
	assert user.last_name == 'User'
	assert user.bio == 'This is an updated test user.'
	assert user.profile_picture == 'updated_profile_picture.jpg'

