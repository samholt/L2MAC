import pytest
from user import User

def test_user_creation():
	user = User('test@test.com', 'password')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert isinstance(user.id, str)
