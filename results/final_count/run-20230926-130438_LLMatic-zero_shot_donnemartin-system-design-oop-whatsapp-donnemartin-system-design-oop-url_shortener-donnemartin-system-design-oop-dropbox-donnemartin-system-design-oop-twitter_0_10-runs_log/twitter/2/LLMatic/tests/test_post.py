import pytest
from post import Post, Comment, create_post, delete_post, like_post, retweet_post, comment_on_post, search_posts, filter_posts, get_timeline, posts_db
from user import register_user, users_db


def test_create_post():
	users_db.clear()
	posts_db.clear()
	register_user('test@test.com', 'testuser', 'testpass')
	assert create_post('testuser', 'test content', ['test.jpg']) == 'Post created successfully'
	assert len(posts_db) == 1
	assert posts_db[1].user.username == 'testuser'
	assert posts_db[1].content == 'test content'
	assert posts_db[1].images == ['test.jpg']


def test_delete_post():
	assert delete_post('testuser', 1) == 'Post deleted successfully'
	assert len(posts_db) == 0


def test_like_post():
	create_post('testuser', 'test content', ['test.jpg'])
	assert like_post('testuser', 1) == 'Post liked'
	assert posts_db[1].likes == 1


def test_retweet_post():
	assert retweet_post('testuser', 1) == 'Post retweeted'
	assert posts_db[1].retweets == 1


def test_comment_on_post():
	assert comment_on_post('testuser', 1, 'test comment') == 'Comment added'
	assert len(posts_db[1].comments) == 1
	assert posts_db[1].comments[0].user.username == 'testuser'
	assert posts_db[1].comments[0].content == 'test comment'


def test_search_posts():
	assert 'testuser' in [post.user.username for post in search_posts('test')]


def test_filter_posts():
	assert len(filter_posts('hashtag', '#test')) == 0


def test_get_timeline():
	register_user('test2@test.com', 'testuser2', 'testpass')
	create_post('testuser2', 'test content 2', ['test2.jpg'])
	assert len(get_timeline('testuser')) == 0

