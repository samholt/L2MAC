import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('test1@test.com', 'test1', 'password1', False), User('test2@test.com', 'test2', 'password2', False)]
	search = Search(users, [])
	assert len(search.search_users('test1')) == 1


def test_search_posts():
	posts = [Post('test1', 'This is a test post'), Post('test2', 'Another test post')]
	search = Search([], posts)
	assert len(search.search_posts('test')) == 2


def test_filter_posts():
	posts = [Post('test1', 'This is a #test post'), Post('test2', 'Another test post @test1')]
	search = Search([], posts)
	assert len(search.filter_posts('hashtag', 'test')) == 1
	assert len(search.filter_posts('user_mention', 'test1')) == 1
	assert len(search.filter_posts('trending_topic', 'test')) == 2
