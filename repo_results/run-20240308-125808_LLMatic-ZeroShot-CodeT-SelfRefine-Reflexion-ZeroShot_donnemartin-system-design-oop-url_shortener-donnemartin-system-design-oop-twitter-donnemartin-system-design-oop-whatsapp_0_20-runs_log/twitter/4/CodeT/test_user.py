import pytest
from user import User

@pytest.fixture
def user():
	return User('test@example.com', 'testuser', 'password')


def test_check_password(user):
	assert user.check_password('password')
	assert not user.check_password('wrongpassword')


def test_to_dict(user):
	user_dict = user.to_dict()
	assert user_dict['email'] == 'test@example.com'
	assert user_dict['username'] == 'testuser'
	assert 'password' not in user_dict
