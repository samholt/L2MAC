from user import User
from post import Post
from search import Search
import pytest


def test_search_users():
	users = [User('email1', 'user1', 'password1'), User('email2', 'user2', 'password2')]
	search = Search(users, [])
	assert search.search_users('user1') == [users[0]]
	assert search.search_users('user3') == []


def test_search_posts():
	users = [User('email1', 'user1', 'password1')]
	posts = [Post(users[0], 'Hello world!'), Post(users[0], 'Another post')]
	search = Search(users, posts)
	assert search.search_posts('Hello') == [posts[0]]
	assert search.search_posts('post') == [posts[1]]


def test_filter_posts():
	users = [User('email1', 'user1', 'password1')]
	posts = [Post(users[0], 'Hello world! #greeting'), Post(users[0], 'Another post @user1')]
	search = Search(users, posts)
	assert search.filter_posts('hashtag', 'greeting') == [posts[0]]
	assert search.filter_posts('mention', 'user1') == [posts[1]]
	assert search.filter_posts('trending', '') == []

	posts[0].likes = 101
	assert search.filter_posts('trending', '') == [posts[0]]
