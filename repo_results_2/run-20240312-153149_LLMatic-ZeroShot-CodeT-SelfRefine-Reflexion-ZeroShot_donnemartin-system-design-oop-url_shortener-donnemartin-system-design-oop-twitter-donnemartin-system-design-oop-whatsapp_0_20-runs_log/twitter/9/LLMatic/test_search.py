import pytest
from user import User
from post import Post
from search import Search


def test_search():
	user_obj = User()
	post_obj = Post()
	search_obj = Search(user_obj, post_obj)
	user_obj.register('test@test.com', 'testuser', 'password')
	post_obj.create_post('testuser', 'This is a test post', '')
	users, posts = search_obj.search('test')
	assert 'testuser' in users
	assert 'This is a test post' in [post['content'] for post in posts]


def test_filter_posts():
	user_obj = User()
	post_obj = Post()
	search_obj = Search(user_obj, post_obj)
	user_obj.register('test@test.com', 'testuser', 'password')
	post_obj.create_post('testuser', 'This is a #test post', '')
	posts = search_obj.filter_posts('#test')
	assert 'This is a #test post' in [post['content'] for post in posts]
