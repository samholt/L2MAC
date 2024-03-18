import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	user1 = User('user1', 'user1@example.com', 'password1')
	user2 = User('user2', 'user2@example.com', 'password2')
	search = Search([user1, user2], [])
	assert search.search_users('user1') == [user1]


def test_search_posts():
	post1 = Post('Hello world', [], 'user1')
	post2 = Post('Hello user2', [], 'user2')
	search = Search([], [post1, post2])
	assert search.search_posts('Hello') == [post1, post2]


def test_filter_posts():
	post1 = Post('#Hello world', [], 'user1')
	post2 = Post('@user2 Hello', [], 'user2')
	search = Search([], [post1, post2])
	assert search.filter_posts('hashtag', '#Hello') == [post1]
	assert search.filter_posts('user_mention', '@user2') == [post2]
	assert search.filter_posts('trending_topic', 'Hello') == [post1, post2]
