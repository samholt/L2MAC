from user import User
import pytest

def test_user_creation():
	user = User('Alice', 'password', 'alice.jpg', 'Hello, I am Alice', 'public')
	assert user.email == 'Alice'
	assert user.password == 'password'
	assert user.profile_picture == 'alice.jpg'
	assert user.status_message == 'Hello, I am Alice'
	assert user.privacy_settings == 'public'
	assert user.is_online == False

def test_user_online_status():
	user = User('Alice', 'password', 'alice.jpg', 'Hello, I am Alice', 'public')
	user.set_online_status(True)
	assert user.get_online_status() == True

	user.set_online_status(False)
	assert user.get_online_status() == False
