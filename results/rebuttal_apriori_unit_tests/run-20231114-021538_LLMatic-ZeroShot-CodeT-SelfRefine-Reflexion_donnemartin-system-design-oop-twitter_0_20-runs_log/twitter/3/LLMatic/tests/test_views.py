import pytest
from views import create_post, delete_post, like_post, retweet_post, reply_to_post, search_posts, search_users, follow_user, unfollow_user, send_message, get_notifications, get_trending_topics, get_user_recommendations


def test_create_post():
	assert create_post(1, 'Hello, world!') is not None


def test_delete_post():
	post = create_post(1, 'Hello, world!')
	assert delete_post(1, post.id) is True


def test_like_post():
	post = create_post(1, 'Hello, world!')
	assert like_post(1, post.id) is not None


def test_retweet_post():
	post = create_post(1, 'Hello, world!')
	assert retweet_post(1, post.id) is not None


def test_reply_to_post():
	post = create_post(1, 'Hello, world!')
	assert reply_to_post(1, post.id, 'Hello, back!') is not None


def test_search_posts():
	assert search_posts('Hello') is not None


def test_search_users():
	assert search_users('user1') is not None


def test_follow_user():
	assert follow_user(1, 2) is True


def test_unfollow_user():
	assert unfollow_user(1, 2) is True


def test_send_message():
	assert send_message(1, 2, 'Hello, user2!') is not None


def test_get_notifications():
	assert get_notifications(1) is not None


def test_get_trending_topics():
	assert get_trending_topics() is not None


def test_get_user_recommendations():
	assert get_user_recommendations(1) is not None
