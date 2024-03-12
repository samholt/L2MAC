import pytest
from post import Post


def test_create_post():
	post = Post('user1', 'This is a test post')
	assert post.create() == 'Post created successfully'


def test_create_post_with_image():
	post = Post('user1', 'This is a test post', 'image.jpg')
	assert post.create() == 'Post created successfully'


def test_create_post_exceeding_character_limit():
	post = Post('user1', 'a' * 281)
	assert post.create() == 'Post content exceeds 280 characters'


def test_delete_post():
	post = Post('user1', 'This is a test post')
	post.create()
	assert post.delete() == 'Post deleted successfully'


def test_delete_nonexistent_post():
	post = Post('user1', 'This is a test post')
	assert post.delete() == 'Post not found'


def test_like_post():
	post = Post('user1', 'This is a test post')
	post.create()
	assert post.like() == 'Post liked'
	assert post.likes == 1


def test_retweet_post():
	post = Post('user1', 'This is a test post')
	post.create()
	assert post.retweet() == 'Post retweeted'
	assert post.retweets == 1


def test_reply_post():
	post = Post('user1', 'This is a test post')
	post.create()
	reply = post.reply('user2', 'This is a reply')
	assert reply == 'Reply posted'
	assert len(post.replies) == 1
