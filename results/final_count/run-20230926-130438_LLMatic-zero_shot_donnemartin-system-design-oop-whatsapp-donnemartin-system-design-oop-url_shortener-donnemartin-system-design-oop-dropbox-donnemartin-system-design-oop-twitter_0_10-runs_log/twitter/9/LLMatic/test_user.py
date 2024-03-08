import pytest
from user import User, users_db


def test_register():
	user = User('test@test.com', 'testuser', 'testpass')
	assert user.register() == 'User registered successfully'
	assert 'test@test.com' in users_db


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	assert isinstance(user.authenticate('testpass'), str)


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	assert user.reset_password('newpass') == 'Password reset successfully'
	assert user.password == 'newpass'


def test_edit_profile():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	assert user.edit_profile(profile_picture='newpic.jpg', bio='new bio', website_link='newwebsite.com', location='new location') == 'Profile updated successfully'
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'newwebsite.com'
	assert user.location == 'new location'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	assert user.toggle_privacy() == 'Privacy setting updated successfully'
	assert user.private == True
