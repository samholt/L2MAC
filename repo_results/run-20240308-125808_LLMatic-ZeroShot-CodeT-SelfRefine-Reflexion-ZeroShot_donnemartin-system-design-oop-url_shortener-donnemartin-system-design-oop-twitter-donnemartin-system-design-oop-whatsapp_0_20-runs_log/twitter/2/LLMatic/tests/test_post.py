import pytest
from models import User, Post
from views import users, posts


def test_create_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	assert len(posts) == 1
	assert posts[0].content == 'Test content'
	assert posts[0].images == ['image1.jpg', 'image2.jpg']
	assert posts[0].user == user


def test_view_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	assert posts[0].content == 'Test content'
	assert posts[0].images == ['image1.jpg', 'image2.jpg']
	assert posts[0].user == user


def test_delete_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	del posts[0]
	assert len(posts) == 0


def test_like_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	post.likes += 1
	assert posts[0].likes == 1


def test_retweet_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	post.retweets += 1
	assert posts[0].retweets == 1


def test_reply_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post('Test content', ['image1.jpg', 'image2.jpg'], user)
	posts[0] = post
	post.replies.append('Test reply')
	assert posts[0].replies == ['Test reply']
