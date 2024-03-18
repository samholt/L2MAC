import pytest
from search import search, search_user, search_post
from user import register, users_db
from post import create_post

def setup_module(module):
	register('test2@test.com', 'testuser2', 'password', False)
	create_post(users_db['testuser2'], 'This is a test post')

def test_search():
	result = search('test')
	assert 'testuser2' in result['users']
	assert 'This is a test post' in [post.text for post in result['posts']]

def test_search_user():
	assert search_user('testuser2') == users_db['testuser2']

def test_search_post():
	assert search_post('This is a test post') == users_db['testuser2'].posts[0]

def test_search_post_not_found():
	assert search_post('Nonexistent post') == 'Post not found'
