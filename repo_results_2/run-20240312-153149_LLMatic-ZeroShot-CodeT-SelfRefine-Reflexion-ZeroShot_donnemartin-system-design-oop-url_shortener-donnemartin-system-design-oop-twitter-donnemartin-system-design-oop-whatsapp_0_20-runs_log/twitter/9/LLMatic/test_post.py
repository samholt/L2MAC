import pytest
from post import Post

def test_create_post():
	post = Post()
	assert post.create_post('user1', 'Hello World!', 'image.jpg') == 'Post created successfully'


def test_delete_post():
	post = Post()
	post.create_post('user1', 'Hello World!', 'image.jpg')
	assert post.delete_post('user1', 0) == 'Post deleted successfully'


def test_delete_non_existent_post():
	post = Post()
	assert post.delete_post('user1', 0) == 'Post not found'


def test_like_post():
	post = Post()
	post.create_post('user1', 'Hello World!', 'image.jpg')
	assert post.like_post('user1', 0) == 'Post liked successfully'


def test_retweet_post():
	post = Post()
	post.create_post('user1', 'Hello World!', 'image.jpg')
	assert post.retweet_post('user1', 0) == 'Post retweeted successfully'


def test_reply_to_post():
	post = Post()
	post.create_post('user1', 'Hello World!', 'image.jpg')
	assert post.reply_to_post('user1', 0, 'This is a reply') == 'Reply added successfully'
