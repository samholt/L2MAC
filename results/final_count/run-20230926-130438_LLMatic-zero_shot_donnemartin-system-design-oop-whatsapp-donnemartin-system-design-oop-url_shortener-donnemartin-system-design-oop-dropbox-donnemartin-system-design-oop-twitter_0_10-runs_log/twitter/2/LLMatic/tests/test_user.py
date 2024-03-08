import pytest
from user import User, register_user, authenticate_user, edit_profile, search_users, follow_user, unfollow_user, add_notification, users_db


def test_register_user():
	users_db.clear()
	assert register_user('test@test.com', 'testuser', 'testpass') == 'User registered successfully'
	assert 'testuser' in users_db
	assert users_db['testuser'].email == 'test@test.com'
	assert users_db['testuser'].username == 'testuser'
	assert users_db['testuser'].password == 'testpass'


def test_authenticate_user():
	assert authenticate_user('testuser', 'testpass') is not None
	assert authenticate_user('testuser', 'wrongpass') == 'Invalid credentials'
	assert authenticate_user('wronguser', 'testpass') == 'Invalid credentials'


def test_edit_profile():
	assert edit_profile('testuser', 'newpic.jpg', 'new bio', 'newwebsite.com', 'new location', True) == 'Profile updated successfully'
	assert users_db['testuser'].profile_picture == 'newpic.jpg'
	assert users_db['testuser'].bio == 'new bio'
	assert users_db['testuser'].website_link == 'newwebsite.com'
	assert users_db['testuser'].location == 'new location'
	assert users_db['testuser'].is_private == True


def test_search_users():
	assert 'testuser' in [user.username for user in search_users('test')]


def test_follow_user():
	register_user('test2@test.com', 'testuser2', 'testpass')
	assert follow_user('testuser', 'testuser2') == 'User followed successfully'
	assert 'testuser2' in users_db['testuser'].following
	assert 'testuser' in users_db['testuser2'].followers


def test_unfollow_user():
	assert unfollow_user('testuser', 'testuser2') == 'User unfollowed successfully'
	assert 'testuser2' not in users_db['testuser'].following
	assert 'testuser' not in users_db['testuser2'].followers


def test_add_notification():
	assert add_notification('testuser', 'test notification') == 'Notification added'
	assert 'test notification' in users_db['testuser'].notifications

