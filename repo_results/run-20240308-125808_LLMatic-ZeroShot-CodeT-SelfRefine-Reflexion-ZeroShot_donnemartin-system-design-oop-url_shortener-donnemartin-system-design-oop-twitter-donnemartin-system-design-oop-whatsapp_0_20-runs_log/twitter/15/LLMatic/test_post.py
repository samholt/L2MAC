import pytest
from post import Post

def test_create_post():
	db = {}
	post = Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')
	post.create_post(db)
	assert len(db) == 1
	assert db[1] == post

def test_delete_post():
	db = {1: Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')}
	post = Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')
	post.delete_post(1, db)
	assert len(db) == 0

def test_like_post():
	post = Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')
	post.like_post('user2')
	assert 'user2' in post.likes

def test_retweet_post():
	post = Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')
	post.retweet_post('user2')
	assert 'user2' in post.retweets

def test_reply_post():
	post = Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00')
	reply = Post('user2', 'Reply to post', 'image2.jpg', '2022-01-02 00:00:00')
	post.reply_post(reply)
	assert reply in post.replies

def test_search():
	db = {1: Post('user1', 'Hello World!', 'image.jpg', '2022-01-01 00:00:00'), 2: Post('user2', 'Goodbye World!', 'image2.jpg', '2022-01-02 00:00:00')}
	assert len(Post.search('World', db)) == 2
	assert len(Post.search('Hello', db)) == 1

def test_filter_posts():
	db = {1: Post('user1', '#Hello World!', 'image.jpg', '2022-01-01 00:00:00'), 2: Post('user2', 'Goodbye @user1!', 'image2.jpg', '2022-01-02 00:00:00')}
	assert len(Post.filter_posts('#Hello', db)) == 1
	assert len(Post.filter_posts('@user1', db)) == 1

def test_get_trending_topics():
	db = {1: Post('user1', '#Hello World!', 'image.jpg', '2022-01-01 00:00:00'), 2: Post('user2', '#Goodbye #World!', 'image2.jpg', '2022-01-02 00:00:00'), 3: Post('user3', '#Hello #Goodbye #World!', 'image3.jpg', '2022-01-03 00:00:00')}
	assert len(Post.get_trending_topics(db)) == 3
	assert Post.get_trending_topics(db) == ['#Hello', '#Goodbye', '#World!']
