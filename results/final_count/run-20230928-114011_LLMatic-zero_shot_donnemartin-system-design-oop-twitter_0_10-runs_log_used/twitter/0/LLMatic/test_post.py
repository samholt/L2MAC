import pytest
from post import Post


def test_create_post():
	user = 'test_user'
	content = 'test_content'
	image = 'test_image.jpg'
	post = Post.create_post(user, content, image)
	assert post.user == user
	assert post.content == content
	assert post.image == image
	assert post.timestamp is not None


def test_delete_post():
	user = 'test_user'
	content = 'test_content'
	image = 'test_image.jpg'
	post = Post.create_post(user, content, image)
	post.delete_post()
	assert post.user is None
	assert post.content is None
	assert post.image is None
	assert post.timestamp is None


def test_like_post():
	post = Post('test_user', 'test_content')
	post.like()
	assert post.likes == 1


def test_retweet_post():
	post = Post('test_user', 'test_content')
	post.retweet()
	assert post.retweets == 1


def test_reply_post():
	post = Post('test_user', 'test_content')
	reply = post.reply('reply_user', 'reply_content')
	assert reply in post.replies
	assert reply.user == 'reply_user'
	assert reply.content == 'reply_content'
