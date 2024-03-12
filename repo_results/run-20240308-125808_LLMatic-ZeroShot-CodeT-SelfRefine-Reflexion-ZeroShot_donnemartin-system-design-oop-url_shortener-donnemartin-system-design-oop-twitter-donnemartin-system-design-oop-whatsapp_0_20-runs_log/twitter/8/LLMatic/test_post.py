import pytest
from post import Post, posts_db


def test_create_post():
	# Test case: Text length is within the limit
	post1 = Post('user1', 'This is a test post.')
	assert post1.create() == 'Post created successfully.'
	assert posts_db['user1']['text'] == 'This is a test post.'

	# Test case: Text length exceeds the limit
	post2 = Post('user2', 'a'*281)
	assert post2.create() == 'Error: The post text exceeds the limit of 280 characters.'


def test_delete_post():
	# Test case: Post exists
	post1 = Post('user1', 'This is a test post.')
	assert post1.delete() == 'Post deleted successfully.'
	assert 'user1' not in posts_db

	# Test case: Post does not exist
	post3 = Post('user3', 'This is another test post.')
	assert post3.delete() == 'Error: Post not found.'


def test_like_post():
	# Test case: Like a post
	post1 = Post('user1', 'This is a test post.')
	post1.create()
	post1.like()
	assert posts_db['user1']['likes'] == 1


def test_retweet_post():
	# Test case: Retweet a post
	post1 = Post('user1', 'This is a test post.')
	post1.create()
	post1.retweet()
	assert posts_db['user1']['retweets'] == 1


def test_reply_post():
	# Test case: Reply to a post
	post1 = Post('user1', 'This is a test post.')
	post1.create()
	post2 = Post('user2', 'This is a reply.')
	post1.reply(post2.user_id, post2.text)
	assert posts_db['user2']['text'] == 'This is a reply.'
	assert post2.user_id in posts_db['user1']['replies']
