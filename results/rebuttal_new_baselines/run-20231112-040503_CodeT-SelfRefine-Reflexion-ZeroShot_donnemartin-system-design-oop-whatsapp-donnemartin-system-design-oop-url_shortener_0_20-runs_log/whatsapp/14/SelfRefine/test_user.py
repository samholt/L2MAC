import pytest
from user import User


def test_user():
	user = User('test@test.com', 'test')
	assert user.email == 'test@test.com'
	assert user.password == 'test'
	assert user.id is not None
