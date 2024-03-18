import pytest
from post import Post
from datetime import datetime


def test_create_post():
	user = 'test_user'
	content = 'This is a test post'
	image = 'test_image.jpg'
	post = Post(user, content, image)
	result = post.create()
	assert result['user'] == user
	assert result['content'] == content
	assert result['image'] == image
	assert datetime.strptime(result['timestamp'], '%Y-%m-%d %H:%M:%S.%f')


def test_delete_post():
	post = Post('test_user', 'This is a test post', 'test_image.jpg')
	result = post.delete()
	assert result['status'] == 'Post deleted'
	assert post.user is None
	assert post.content is None
	assert post.image is None
	assert post.timestamp is None


def test_like_post():
	post = Post('test_user', 'This is a test post')
	result = post.like()
	assert result['status'] == 'Post liked'
	assert result['likes'] == 1


def test_retweet_post():
	post = Post('test_user', 'This is a test post')
	result = post.retweet()
	assert result['status'] == 'Post retweeted'
	assert result['retweets'] == 1


def test_reply_post():
	post = Post('test_user', 'This is a test post')
	user = 'reply_user'
	content = 'This is a reply'
	result = post.reply(user, content)
	assert result['status'] == 'Reply posted'
	assert result['reply']['user'] == user
	assert result['reply']['content'] == content
