import pytest
from cloudsafe.user.views import register, login, update_profile

def test_register():
	response = register()
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'

def test_login():
	response = login()
	assert response.status_code in [200, 401]

def test_update_profile():
	response = update_profile()
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Profile updated successfully'
