import pytest
from post import Post
from user import User

def test_post_creation():
	user = User('test_user', 'test_password', 'test_bio', False)
	post = Post('test_text', ['test_image'], user)
	assert post.text == 'test_text'
	assert post.images == ['test_image']
	assert post.author == user
	assert post.timestamp is not None
	assert post.likes == 0
	assert post.retweets == 0
	assert post.replies == []

def test_post_deletion():
	user = User('test_user', 'test_password', 'test_bio', False)
	post = Post('test_text', ['test_image'], user)
	post.delete_post()
	assert post.text is None
	assert post.images is None
	assert post.author is None
	assert post.timestamp is None

def test_post_interaction():
	user = User('test_user', 'test_password', 'test_bio', False)
	post = Post('test_text', ['test_image'], user)
	post.like_post()
	post.retweet_post()
	reply = Post('reply_text', [], user)
	post.reply_to_post(reply)
	assert post.likes == 1
	assert post.retweets == 1
	assert post.replies == [reply]

