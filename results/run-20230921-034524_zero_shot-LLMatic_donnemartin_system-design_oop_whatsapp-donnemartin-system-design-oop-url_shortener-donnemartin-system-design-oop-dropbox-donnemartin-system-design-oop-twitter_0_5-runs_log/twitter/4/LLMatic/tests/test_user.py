import pytest
from models.user import User
from controllers.user_controller import UserController


def test_user_creation():
	user_controller = UserController()
	user = user_controller.create_user('testuser', 'testpassword')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'


def test_user_following():
	user_controller = UserController()
	user1 = user_controller.create_user('user1', 'password1')
	user2 = user_controller.create_user('user2', 'password2')
	user_controller.follow_user('user1', 'user2')
	assert user2 in user1.following
	assert user1 in user2.followers
