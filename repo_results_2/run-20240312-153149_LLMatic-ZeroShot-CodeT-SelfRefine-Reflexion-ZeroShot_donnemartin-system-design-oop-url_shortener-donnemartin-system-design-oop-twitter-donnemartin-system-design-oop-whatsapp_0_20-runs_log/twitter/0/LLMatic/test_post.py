import pytest
from post import Post
from user import User


def test_create_post():
	Post.posts.clear()
	Post.create_post('Test Title', 'Test Content', 1)
	assert len(Post.posts) == 1


def test_delete_post():
	Post.posts.clear()
	Post.create_post('Test Title', 'Test Content', 1)
	assert Post.delete_post(1) == True
	assert len(Post.posts) == 0


def test_like_post():
	Post.posts.clear()
	post = Post.create_post('Test Title', 'Test Content', 1)
	post.like_post()
	assert post.likes == 1


def test_retweet_post():
	Post.posts.clear()
	post = Post.create_post('Test Title', 'Test Content', 1)
	post.retweet_post()
	assert post.retweets == 1


def test_reply_post():
	Post.posts.clear()
	post = Post.create_post('Test Title', 'Test Content', 1)
	post.reply_post('Test Reply')
	assert len(post.replies) == 1


def test_search_posts():
	Post.posts.clear()
	Post.create_post('Test Title', 'Test Content', 1)
	Post.create_post('Another Title', 'Another Content', 2)
	results = Post.search_posts('Test')
	assert len(results) == 1
	assert results[0].title == 'Test Title'


def test_trending_topics():
	Post.posts.clear()
	Post.create_post('Test Title', '#Test Content', 1)
	Post.create_post('Another Title', '#Another Content', 2)
	Post.create_post('Third Title', '#Test Content', 3)
	trending = Post.trending_topics()
	assert len(trending) == 2
	assert trending[0][0] == '#Test'
	assert trending[0][1] == 2


def test_recommend_users():
	User.users.clear()
	User(1, 'test1@test.com', 'test1', 'password')
	User(2, 'test2@test.com', 'test2', 'password')
	User(3, 'test3@test.com', 'test3', 'password')
	User.users[1].follow(2)
	User.users[2].follow(3)
	recommended = User.users[1].recommend_users()
	assert len(recommended) == 1
	assert recommended[0].id == 3
