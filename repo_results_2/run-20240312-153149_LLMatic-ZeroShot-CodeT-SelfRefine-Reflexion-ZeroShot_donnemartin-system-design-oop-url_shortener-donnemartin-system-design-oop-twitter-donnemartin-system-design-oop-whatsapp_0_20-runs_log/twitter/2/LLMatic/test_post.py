import pytest
from post import Post, create_post, post_db
from user import User, users_db, register

def test_create_post():
	register('user1@test.com', 'user1', 'pass1', False)
	new_post = create_post(users_db['user1'], 'Hello World')
	assert new_post == 'Post created successfully'


def test_like_post():
	register('user1@test.com', 'user1', 'pass1', False)
	register('user2@test.com', 'user2', 'pass2', False)
	create_post(users_db['user1'], 'Hello World')
	assert users_db['user2'].like(post_db['user1'][0]) == 'Post liked'


def test_retweet_post():
	register('user1@test.com', 'user1', 'pass1', False)
	register('user2@test.com', 'user2', 'pass2', False)
	create_post(users_db['user1'], 'Hello World')
	assert users_db['user2'].retweet(post_db['user1'][0]) == 'Post retweeted'


def test_reply_post():
	register('user1@test.com', 'user1', 'pass1', False)
	register('user2@test.com', 'user2', 'pass2', False)
	create_post(users_db['user1'], 'Hello World')
	assert users_db['user2'].reply(post_db['user1'][0], 'Nice post!') == 'Reply posted'
