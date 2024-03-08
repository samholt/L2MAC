import pytest
from users import UserManager


def test_follow_user():
	user_manager = UserManager()
	user_manager.create_user('user1', 'password1')
	user_manager.create_user('user2', 'password2')
	assert user_manager.follow_user('user1', 'user2') == 'User followed successfully'
	assert user_manager.follow_user('user1', 'user2') == 'User already followed'
	assert user_manager.follow_user('user1', 'user3') == 'User not found'


def test_get_feed():
	user_manager = UserManager()
	user_manager.create_user('user1', 'password1')
	user_manager.create_user('user2', 'password2')
	user1 = user_manager.get_user('user1')
	user2 = user_manager.get_user('user2')
	user1.activity_feed.append({'timestamp': '2022-01-01', 'activity': 'Submitted a recipe'})
	user2.activity_feed.append({'timestamp': '2022-01-02', 'activity': 'Submitted a recipe'})
	user_manager.follow_user('user1', 'user2')
	feed = user_manager.get_feed('user1')
	assert len(feed) == 1
	assert feed[0]['timestamp'] == '2022-01-02'
