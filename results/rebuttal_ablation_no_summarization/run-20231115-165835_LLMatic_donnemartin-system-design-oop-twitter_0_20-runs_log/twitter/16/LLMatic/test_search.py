import pytest
from user import User
from post import Post
from search import Search


def test_search():
	user_db = {}
	post_db = Post()
	search = Search(user_db, post_db)
	user = User('test@test.com', 'testuser', 'password', False, 'profile_picture', 'bio', 'website_link', 'location')
	user.register(user_db)
	post_db.create('testuser', 'test post', 'image')
	assert 'testuser' in [user.username for user in search.search('test')['users']]
	assert 'test post' in [post['text'] for post in search.search('test')['posts']]


def test_filter():
	user_db = {}
	post_db = Post()
	search = Search(user_db, post_db)
	post_db.create('testuser', 'test post', 'image')
	assert 'test post' in [post['text'] for post in search.filter('test')]
