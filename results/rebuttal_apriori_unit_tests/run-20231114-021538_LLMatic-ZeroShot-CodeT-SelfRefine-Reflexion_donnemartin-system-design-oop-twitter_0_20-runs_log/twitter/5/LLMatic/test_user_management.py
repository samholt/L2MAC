import pytest
from user_management import register_user, authenticate_user, edit_user_profile, search_users, follow_user, unfollow_user, get_user_notifications


def test_register_user():
	assert register_user('testuser', 'testuser@example.com', 'password') == True


def test_authenticate_user():
	register_user('testuser', 'testuser@example.com', 'password')
	assert authenticate_user('testuser@example.com', 'password') != False


def test_edit_user_profile():
	register_user('testuser', 'testuser@example.com', 'password')
	assert edit_user_profile('testuser', 'new bio', 'new website', 'new location') == True


def test_search_users():
	register_user('testuser', 'testuser@example.com', 'password')
	assert len(search_users('testuser')) > 0


def test_follow_unfollow_user():
	register_user('user1', 'user1@example.com', 'password')
	register_user('user2', 'user2@example.com', 'password')
	assert follow_user('user1', 'user2') == True
	assert unfollow_user('user1', 'user2') == True


def test_get_user_notifications():
	register_user('user3', 'user3@example.com', 'password')
	register_user('user4', 'user4@example.com', 'password')
	follow_user('user3', 'user4')
	unfollow_user('user3', 'user4')
	assert len(get_user_notifications('user3')) == 2
	assert len(get_user_notifications('user3')) == 0

