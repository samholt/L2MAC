import pytest
from user import User
from post import Post
from search import search, filter

def test_search():
	db = {}
	user1 = User('test1@test.com', 'test1', 'password', False, 'Test User 1')
	user1.register(db)
	post1 = Post(user1, 'This is a test post')
	post1.create(db)
	results = search('test', db)
	assert len(results['users']) == 1
	assert len(results['posts']) == 1

def test_filter():
	db = {}
	user1 = User('test1@test.com', 'test1', 'password', False, 'Test User 1')
	user1.register(db)
	post1 = Post(user1, 'This is a #test post')
	post1.create(db)
	results = filter('#test', db)
	assert len(results) == 1
