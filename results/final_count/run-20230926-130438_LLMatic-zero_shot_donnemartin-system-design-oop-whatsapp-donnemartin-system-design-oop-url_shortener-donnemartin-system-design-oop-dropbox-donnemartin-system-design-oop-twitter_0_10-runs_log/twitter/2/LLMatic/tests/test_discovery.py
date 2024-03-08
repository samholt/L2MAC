import pytest
from user import register_user, users_db
from post import create_post, posts_db
from discovery import get_trending_topics, recommend_users


def setup_module():
	# Populate the mock database before the tests are run
	register_user('test@test.com', 'testuser', 'testpassword')
	register_user('test2@test.com', 'testuser2', 'testpassword2')
	create_post('testuser', 'Hello #world', [])
	create_post('testuser2', 'Hello #world', [])


def test_get_trending_topics():
	assert get_trending_topics() == [('#world', 2)]


def test_recommend_users():
	assert recommend_users('testuser') == ['testuser2']
	assert recommend_users('wronguser') == 'User not found'
