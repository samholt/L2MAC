import pytest
from trending import trending
from post import create_post, post_db
from user import User, register


def setup_module(module):
	post_db.clear()
	register('user1@test.com', 'user1', 'password1', False)
	register('user2@test.com', 'user2', 'password2', False)
	user1 = User('user1@test.com', 'user1', 'password1', False)
	user2 = User('user2@test.com', 'user2', 'password2', False)
	create_post(user1, 'Hello #world')
	create_post(user2, 'Hello #world #python')
	create_post(user1, 'Hello #python #world')


def test_trending():
	assert trending() == [('#world', 3), ('#python', 2)]
	assert trending('#world') == [('#world', 3)]
	assert trending('#python') == [('#python', 2)]
