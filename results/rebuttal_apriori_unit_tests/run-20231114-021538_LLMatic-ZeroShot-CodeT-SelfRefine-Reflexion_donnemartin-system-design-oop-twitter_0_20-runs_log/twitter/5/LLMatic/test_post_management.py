import pytest
from post_management import create_post, delete_post, like_post, retweet_post, reply_to_post, search_posts


def test_create_post():
	assert create_post(1, 'This is a test post') is not None


def test_delete_post():
	post_id = create_post(1, 'This is a test post')
	assert delete_post(1, post_id) == True


def test_like_post():
	post_id = create_post(1, 'This is a test post')
	assert like_post(1, post_id) == True


def test_retweet_post():
	post_id = create_post(1, 'This is a test post')
	assert retweet_post(1, post_id) == True


def test_reply_to_post():
	post_id = create_post(1, 'This is a test post')
	assert reply_to_post(1, post_id, 'This is a reply') == True


def test_search_posts():
	post_id = create_post(1, 'This is a test post')
	assert len(search_posts('test')) > 0
