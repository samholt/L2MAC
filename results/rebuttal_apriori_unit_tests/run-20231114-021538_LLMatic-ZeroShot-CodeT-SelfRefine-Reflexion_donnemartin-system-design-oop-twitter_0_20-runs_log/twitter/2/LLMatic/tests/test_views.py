import pytest
from views import register_user, authenticate_user, create_post, search_posts, search_users


def test_search_posts():
	register_user('testuser', 'testuser@example.com', 'password')
	token = authenticate_user('testuser@example.com', 'password')
	create_post(token, 'This is a test post')
	results = search_posts('test')
	assert len(results) > 0
	assert 'test' in results[0].content


def test_search_users():
	register_user('testuser', 'testuser@example.com', 'password')
	results = search_users('test')
	assert len(results) > 0
	assert 'test' in results[0].username

