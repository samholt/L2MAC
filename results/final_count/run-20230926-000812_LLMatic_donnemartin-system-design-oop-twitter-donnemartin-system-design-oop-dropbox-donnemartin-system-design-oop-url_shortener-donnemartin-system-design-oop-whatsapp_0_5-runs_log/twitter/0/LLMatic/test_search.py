import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('email', 'username', 'password', False) for _ in range(10)]
	search = Search(users, [])
	assert len(search.search_users('username')) == 10


def test_search_posts():
	users = [User('email', 'username', 'password', False) for _ in range(10)]
	posts = [Post('text', [], users[i]) for i in range(10)]
	search = Search(users, posts)
	assert len(search.search_posts('text')) == 10


def test_filter_posts():
	users = [User('email', 'username', 'password', False) for _ in range(10)]
	posts = [Post('#hashtag', [], users[i]) for i in range(10)]
	search = Search(users, posts)
	assert len(search.filter_posts('hashtag', '#hashtag')) == 10
	assert len(search.filter_posts('user_mention', 'username')) == 10
	assert len(search.filter_posts('trending_topic', '')) == 10
