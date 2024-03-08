import pytest
from post import Post, create_post, delete_post, mock_db, search, filter_posts, get_trending_topics

def test_create_post():
	post = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	create_post(post)
	assert post == mock_db['2022-01-01T00:00:00Z']

def test_delete_post():
	post = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	create_post(post)
	delete_post('2022-01-01T00:00:00Z')
	assert '2022-01-01T00:00:00Z' not in mock_db

def test_like_post():
	post = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	post.like_post()
	assert post.likes == 1

def test_retweet():
	post = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	post.retweet('user2')
	assert 'user2' in post.retweets

def test_reply():
	post = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	post.reply('user2', 'Nice post!')
	assert {'user': 'user2', 'text': 'Nice post!'} in post.replies

def test_search():
	post1 = Post('user1', 'Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	post2 = Post('user2', 'Goodbye World', 'image.jpg', '2022-01-02T00:00:00Z')
	create_post(post1)
	create_post(post2)
	assert post1 in search('Hello')
	assert post2 not in search('Hello')

def test_filter_posts():
	post1 = Post('user1', '#Hello World', 'image.jpg', '2022-01-01T00:00:00Z')
	post2 = Post('user2', 'Goodbye World', 'image.jpg', '2022-01-02T00:00:00Z')
	create_post(post1)
	create_post(post2)
	assert post1 in filter_posts('#Hello')
	assert post2 not in filter_posts('#Hello')

def test_get_trending_topics():
	post1 = Post('user1', '#Hello #World', 'image.jpg', '2022-01-01T00:00:00Z')
	post2 = Post('user2', '#Goodbye #World', 'image.jpg', '2022-01-02T00:00:00Z')
	create_post(post1)
	create_post(post2)
	trending_topics = get_trending_topics()
	assert '#World' in trending_topics
	assert '#Hello' in trending_topics
	assert '#Goodbye' in trending_topics

