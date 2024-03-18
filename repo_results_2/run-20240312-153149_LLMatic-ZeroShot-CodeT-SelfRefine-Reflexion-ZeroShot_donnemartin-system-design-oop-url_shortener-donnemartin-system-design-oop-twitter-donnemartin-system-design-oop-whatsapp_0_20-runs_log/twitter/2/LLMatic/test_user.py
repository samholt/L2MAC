import pytest
from user import register, authenticate, reset_password, users_db, User


def test_register():
	user = register('test@test.com', 'testuser', 'testpass', False)
	assert isinstance(user, User)
	assert user.email == 'test@test.com'
	assert user.username == 'testuser'
	assert user.password == 'testpass'
	assert user.is_private == False


def test_authenticate():
	assert authenticate('testuser', 'testpass') == 'User authenticated'
	assert authenticate('testuser', 'wrongpass') == 'Authentication failed'
	assert authenticate('wronguser', 'testpass') == 'Authentication failed'


def test_reset_password():
	assert reset_password('testuser', 'newpass') == 'Password reset successful'
	assert authenticate('testuser', 'newpass') == 'User authenticated'
	assert authenticate('testuser', 'testpass') == 'Authentication failed'
	assert reset_password('wronguser', 'newpass') == 'User does not exist'

