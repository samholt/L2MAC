import pytest
from models import User, Post
from database import users, posts


def test_create_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post(user, 'Test content')
	posts.append(post)
	assert post in posts


def test_delete_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post(user, 'Test content')
	posts.append(post)
	post.delete()
	posts.remove(post)
	assert post not in posts


def test_like_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post(user, 'Test content')
	posts.append(post)
	post.like()
	assert post.likes == 1


def test_retweet_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post(user, 'Test content')
	posts.append(post)
	post.retweet()
	assert post.retweets == 1


def test_reply_post():
	user = User('test@test.com', 'test', 'test')
	users['test@test.com'] = user
	post = Post(user, 'Test content')
	posts.append(post)
	post.reply(user, 'Test reply')
	assert post.replies == [{'user': user, 'content': 'Test reply'}]
