import pytest
from post import Post
from user import User

user = User('1', 'johndoe@example.com', 'John Doe', 'password', False)


def test_post_creation():
	post = Post.create('1', 'Hello, world!', [], user.id, '2022-01-01 00:00:00')
	assert post.text == 'Hello, world!'
	assert post.author_id == user.id


def test_post_deletion():
	posts_db = {}
	post = Post.create('1', 'Hello, world!', [], user.id, '2022-01-01 00:00:00')
	posts_db['1'] = post
	assert Post.delete(posts_db, '1')
	assert '1' not in posts_db


def test_post_like():
	post = Post('1', 'Hello, world!', [], user.id, '2022-01-01 00:00:00')
	post.like()
	assert post.likes == 1


def test_post_retweet():
	post = Post('1', 'Hello, world!', [], user.id, '2022-01-01 00:00:00')
	post.retweet()
	assert post.retweets == 1


def test_post_reply():
	post = Post('1', 'Hello, world!', [], user.id, '2022-01-01 00:00:00')
	reply = Post('2', 'This is a reply', [], user.id, '2022-01-01 00:01:00')
	post.reply(reply)
	assert post.replies == [reply]
