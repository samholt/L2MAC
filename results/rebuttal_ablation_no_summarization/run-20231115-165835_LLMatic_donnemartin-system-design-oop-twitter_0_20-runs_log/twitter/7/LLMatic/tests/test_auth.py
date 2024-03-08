import pytest
import auth


def test_register_user():
	user = auth.register_user('test@test.com', 'testuser', 'testpass')
	assert user.email == 'test@test.com'
	assert user.username == 'testuser'
	assert user.password == 'testpass'


def test_authenticate_user():
	token = auth.authenticate_user('testuser', 'testpass')
	assert token != ''


def test_update_profile():
	user = auth.update_profile('testuser', 'pic.jpg', 'bio', 'website.com', 'location', 'private')
	assert user.profile_picture == 'pic.jpg'
	assert user.bio == 'bio'
	assert user.website_link == 'website.com'
	assert user.location == 'location'
	assert user.visibility == 'private'


def test_follow_user():
	auth.register_user('test2@test.com', 'testuser2', 'testpass')
	result = auth.follow_user('testuser', 'testuser2')
	assert result
	assert 'testuser2' in auth.users_db['testuser'].following
	assert 'testuser' in auth.users_db['testuser2'].followers


def test_unfollow_user():
	result = auth.unfollow_user('testuser', 'testuser2')
	assert result
	assert 'testuser2' not in auth.users_db['testuser'].following
	assert 'testuser' not in auth.users_db['testuser2'].followers
