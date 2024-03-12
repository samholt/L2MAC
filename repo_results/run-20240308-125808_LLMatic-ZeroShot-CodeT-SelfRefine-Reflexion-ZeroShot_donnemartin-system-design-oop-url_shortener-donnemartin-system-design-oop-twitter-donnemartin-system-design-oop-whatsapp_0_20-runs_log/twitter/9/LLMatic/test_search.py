import pytest
from user import USERS, register
from post import Post
from search import Search


def test_search_users():
	register('test1@example.com', 'test1', 'password', False)
	register('test2@example.com', 'test2', 'password', False)
	register('test3@example.com', 'test3', 'password', False)
	search = Search(USERS, [])
	assert len(search.search_users('test')) == 4
	assert len(search.search_users('1')) == 1


def test_search_posts():
	post1 = Post.create_post('test1@example.com', 'Hello world')
	post2 = Post.create_post('test2@example.com', 'Hello again')
	search = Search({}, [post1, post2])
	assert len(search.search_posts('Hello')) == 2
	assert len(search.search_posts('world')) == 1


def test_filter_posts():
	post1 = Post.create_post('test1@example.com', 'Hello #world')
	post2 = Post.create_post('test2@example.com', 'Hello @test1')
	search = Search({}, [post1, post2])
	assert len(search.filter_posts('hashtag', 'world')) == 1
	assert len(search.filter_posts('user_mention', 'test1')) == 1
	assert len(search.filter_posts('trending_topic', '')) == 2

