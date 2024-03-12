import pytest
from post import Post
from user import User


def test_create_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpass', False)
	id = Post.create(db, 'Hello, world!', ['image1.jpg'], user)
	assert id == 1
	assert db[id].text == 'Hello, world!'
	assert db[id].images == ['image1.jpg']
	assert db[id].author == user


def test_delete_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpass', False)
	id = Post.create(db, 'Hello, world!', ['image1.jpg'], user)
	assert Post.delete(db, id) == 'Post deleted'
	assert Post.delete(db, id) == 'Post not found'


def test_like_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpass', False)
	liker = User('test2@test.com', 'testuser2', 'testpass', False)
	id = Post.create(db, 'Hello, world!', ['image1.jpg'], user)
	db[id].like(liker)
	assert db[id].likes == 1


def test_retweet_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpass', False)
	retweeter = User('test2@test.com', 'testuser2', 'testpass', False)
	id = Post.create(db, 'Hello, world!', ['image1.jpg'], user)
	db[id].retweet(retweeter)
	assert db[id].retweets == 1


def test_reply_post():
	db = {}
	user = User('test@test.com', 'testuser', 'testpass', False)
	replier = User('test2@test.com', 'testuser2', 'testpass', False)
	id = Post.create(db, 'Hello, world!', ['image1.jpg'], user)
	db[id].reply(replier, 'This is a reply.')
	assert db[id].replies == ['This is a reply.']

