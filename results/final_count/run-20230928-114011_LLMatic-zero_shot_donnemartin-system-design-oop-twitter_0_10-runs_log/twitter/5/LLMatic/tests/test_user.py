import pytest
from user import User, UserProfile


def test_user_auth_token():
	user = User('test@test.com', 'testuser', 'testpass')
	token = user.generate_auth_token()
	assert token is not None


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass')
	user.reset_password('newpass')
	assert user.password == 'newpass'


def test_user_profile():
	user = User('test@test.com', 'testuser', 'testpass')
	profile = UserProfile(user, 'pic.jpg', 'bio', 'website.com', 'location')
	assert profile.user == user
	assert profile.profile_picture == 'pic.jpg'
	assert profile.bio == 'bio'
	assert profile.website_link == 'website.com'
	assert profile.location == 'location'
	assert profile.is_private == False


def test_edit_profile():
	user = User('test@test.com', 'testuser', 'testpass')
	profile = UserProfile(user, 'pic.jpg', 'bio', 'website.com', 'location')
	profile.edit_profile('newpic.jpg', 'newbio', 'newwebsite.com', 'newlocation')
	assert profile.profile_picture == 'newpic.jpg'
	assert profile.bio == 'newbio'
	assert profile.website_link == 'newwebsite.com'
	assert profile.location == 'newlocation'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpass')
	profile = UserProfile(user, 'pic.jpg', 'bio', 'website.com', 'location')
	profile.toggle_privacy()
	assert profile.is_private == True
