import pytest
from cloudsafe.app.models import User
from cloudsafe.app.user_service import UserService


def test_user_service():
	user_service = UserService()

	# Register a user
	assert user_service.register_user(1, 'John Doe', 'john@example.com', 'password', 'profile.jpg') == 'User registered successfully'

	# Login the user
	assert user_service.login_user('john@example.com', 'password') == 'Login successful'

	# Change the user's password
	assert user_service.change_password('john@example.com', 'password', 'new_password') == 'Password changed successfully'

	# Update the user's profile picture
	assert user_service.update_profile_picture('john@example.com', 'new_profile.jpg') == 'Profile picture updated successfully'
