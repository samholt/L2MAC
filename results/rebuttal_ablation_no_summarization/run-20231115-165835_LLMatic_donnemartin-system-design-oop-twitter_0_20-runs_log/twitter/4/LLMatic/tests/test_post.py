import pytest
from post import Post
from user import User


def test_create_post():
	user = User('test@test.com', 'testuser', 'password')
	post = Post('This is a test post', [], user)
	post.create_post()


def test_delete_post():
	user = User('test@test.com', 'testuser', 'password')
	post = Post('This is a test post', [], user)
	post.delete_post()


def test_like_post():
	user = User('test@test.com', 'testuser', 'password')
	post = Post('This is a test post', [], user)
	post.like_post()
	assert post.likes == 1


def test_retweet_post():
	user = User('test@test.com', 'testuser', 'password')
	post = Post('This is a test post', [], user)
	post.retweet_post()
	assert post.retweets == 1


def test_reply_to_post():
	user = User('test@test.com', 'testuser', 'password')
	post = Post('This is a test post', [], user)
	reply = 'This is a test reply'
	post.reply_to_post(reply)
	assert post.replies == [reply]
