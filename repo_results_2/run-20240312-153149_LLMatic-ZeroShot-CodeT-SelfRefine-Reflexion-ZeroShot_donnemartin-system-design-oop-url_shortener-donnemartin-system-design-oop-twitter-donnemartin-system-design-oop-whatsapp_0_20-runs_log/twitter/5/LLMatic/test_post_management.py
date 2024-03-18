import pytest
from post_management import PostManagement


def test_create_post():
	pm = PostManagement()
	post = pm.create_post('user1', 'Hello, world!')
	assert post == {'content': 'Hello, world!', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}


def test_delete_post():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world!')
	post = pm.delete_post('user1', 0)
	assert post == {'content': 'Hello, world!', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}


def test_like_post():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world!')
	post = pm.like_post('user1', 0)
	assert post['likes'] == 1


def test_retweet_post():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world!')
	post = pm.retweet_post('user1', 0)
	assert post['retweets'] == 1


def test_reply_to_post():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world!')
	reply = pm.reply_to_post('user1', 0, 'Hello, user1!')
	assert reply == {'content': 'Hello, user1!', 'likes': 0, 'retweets': 0, 'replies': []}


def test_search_posts():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world!')
	result = pm.search_posts('Hello')
	assert result == [{'content': 'Hello, world!', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}]


def test_filter_posts_by_hashtag():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world! #greeting')
	result = pm.filter_posts_by_hashtag('#greeting')
	assert result == [{'content': 'Hello, world! #greeting', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}]


def test_filter_posts_by_user_mention():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, @user2!')
	result = pm.filter_posts_by_user_mention('user2')
	assert result == [{'content': 'Hello, @user2!', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}]


def test_filter_posts_by_trending_topic():
	pm = PostManagement()
	pm.create_post('user1', 'Hello, world! #greeting')
	result = pm.filter_posts_by_trending_topic('#greeting')
	assert result == [{'content': 'Hello, world! #greeting', 'image': None, 'likes': 0, 'retweets': 0, 'replies': []}]
