import pytest
from user import search_users, register_user
from post import search_posts, create_post


def test_search_users():
	username = 'test_user'
	register_user(username, 'test@example.com', 'password')
	assert len(search_users(username)) > 0


def test_search_posts():
	content = 'test_content'
	create_post(1, content)
	assert len(search_posts(content)) > 0
