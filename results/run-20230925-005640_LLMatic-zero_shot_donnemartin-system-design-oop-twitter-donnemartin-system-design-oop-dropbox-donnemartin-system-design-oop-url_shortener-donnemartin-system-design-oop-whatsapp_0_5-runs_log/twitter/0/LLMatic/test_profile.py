import pytest
import profile
import database


def test_profile_management():
	# Register a new user
	response = profile.app.test_client().post('/register', json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'})
	assert response.status_code == 200
	# Login the user
	response = profile.app.test_client().post('/login', json={'username': 'testuser', 'password': 'testpassword'})
	assert response.status_code == 200
	access_token = response.get_json()['access_token']
	# Get the user profile
	response = profile.app.test_client().get('/profile', headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 200
	# Update the user profile
	response = profile.app.test_client().put('/profile', headers={'Authorization': f'Bearer {access_token}'}, json={'bio': 'This is a test user'})
	assert response.status_code == 200
	# Get the updated user profile
	response = profile.app.test_client().get('/profile', headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 200
	assert response.get_json()['bio'] == 'This is a test user'

