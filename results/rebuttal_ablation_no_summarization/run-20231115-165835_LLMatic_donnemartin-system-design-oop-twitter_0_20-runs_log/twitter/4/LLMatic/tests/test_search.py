import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('test1@test.com', 'test1', 'password1'), User('test2@test.com', 'test2', 'password2')]
	search = Search(users, [])
	assert search.search_users('test1') == [users[0]]


def test_search_posts():
	user = User('test@test.com', 'test', 'password')
	posts = [Post('This is a test post', [], user), Post('Another test post', [], user)]
	search = Search([], posts)
	assert search.search_posts('Another') == [posts[1]]


def test_filter_posts():
	user = User('test@test.com', 'test', 'password')
	posts = [Post('This is a #test post', [], user), Post('Another test post', [], user)]
	search = Search([], posts)
	assert search.filter_posts('hashtag', 'test') == [posts[0]]
	assert search.filter_posts('mention', 'test') == []
	assert search.filter_posts('trending', '') == [posts[0], posts[1]]
