import pytest
from user import User


def test_user_creation():
	user = User('test@test.com', 'password')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert user.online == False


def test_set_online_status():
	user = User('test@test.com', 'password')
	user.set_online_status(True)
	assert user.online == True
	user.set_online_status(False)
	assert user.online == False
