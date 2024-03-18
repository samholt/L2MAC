import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('user1', 'pass1'), User('user2', 'pass2')]
	search = Search(users, [])
	assert len(search.search_users('user1')) == 1


def test_search_posts():
	users = [User('user1', 'pass1')]
	posts = [Post('user1', 'post1'), Post('user2', 'post2')]
	search = Search(users, posts)
	assert len(search.search_posts('post1')) == 1


def test_filter_posts():
	users = [User('user1', 'pass1')]
	posts = [Post('user1', '#post1'), Post('user2', '#post2')]
	search = Search(users, posts)
	assert len(search.filter_posts('hashtag', 'post1')) == 1
