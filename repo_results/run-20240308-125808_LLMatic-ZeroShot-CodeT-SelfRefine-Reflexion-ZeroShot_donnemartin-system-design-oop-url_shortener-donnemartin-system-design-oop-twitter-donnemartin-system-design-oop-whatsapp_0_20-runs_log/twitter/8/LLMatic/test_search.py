import pytest
from search import Search
from user import User
from post import Post, posts_db

# Mocking a database with an in-memory dictionary
users_db = {}


def test_search_posts():
	# Clear the posts_db before the test
	posts_db.clear()
	user = User('test@test.com', 'testuser', 'password', False)
	user.register(users_db)
	post = Post(user.email, 'This is a test post')
	post.create()
	search = Search(posts_db)
	results = search.search_posts('test')
	assert len(results) == 1
	assert results[0]['text'] == 'This is a test post'


def test_search_users():
	user = User('test@test.com', 'testuser', 'password', False)
	user.register(users_db)
	search = Search(posts_db)
	results = search.search_users('testuser', users_db)
	assert len(results) == 1
	assert results[0].username == 'testuser'


def test_filter_posts():
	# Clear the posts_db before the test
	posts_db.clear()
	user = User('test@test.com', 'testuser', 'password', False)
	user.register(users_db)
	post = Post(user.email, 'This is a #test post')
	post.create()
	search = Search(posts_db)
	results = search.filter_posts('hashtag', 'test')
	assert len(results) == 1
	assert results[0]['text'] == 'This is a #test post'
