import pytest
from post import Post

def test_create_post():
	post = Post('user1', 'Hello, world!')
	assert post.create_post() == {'user': 'user1', 'text': 'Hello, world!', 'images': [], 'likes': 0, 'retweets': 0, 'replies': []}

def test_delete_post():
	post = Post('user1', 'Hello, world!')
	post.delete_post()
	assert post.create_post() == {'user': 'user1', 'text': None, 'images': None, 'likes': 0, 'retweets': 0, 'replies': []}

def test_like_post():
	post = Post('user1', 'Hello, world!')
	post.like_post()
	assert post.likes == 1

def test_retweet_post():
	post = Post('user1', 'Hello, world!')
	post.retweet_post()
	assert post.retweets == 1

def test_reply_to_post():
	post = Post('user1', 'Hello, world!')
	post.reply_to_post('Hello, user1!')
	assert post.replies == ['Hello, user1!']
