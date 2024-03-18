import pytest
from user import User


def test_user_creation():
	user = User('test@test.com', 'test')
	assert user.email == 'test@test.com'
	assert user.password == 'test'
	assert user.profile_picture == ''
	assert user.status_message == ''
	assert user.privacy_settings == {}
	assert user.blocked_contacts == []
