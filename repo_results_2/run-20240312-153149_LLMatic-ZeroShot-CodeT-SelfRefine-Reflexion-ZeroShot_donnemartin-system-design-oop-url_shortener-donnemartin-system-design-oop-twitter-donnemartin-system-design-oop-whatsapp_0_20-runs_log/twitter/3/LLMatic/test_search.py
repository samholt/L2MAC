import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users_db = {}
	user1 = User('email1', 'username1', 'password1', False)
	user1.register(users_db)
	user2 = User('email2', 'username2', 'password2', False)
	user2.register(users_db)
	search = Search(users_db, {})
	assert search.search_users('username1') == [user1]


def test_search_posts():
	posts_db = {}
	post1 = Post.create_post('username1', 'content1')
	posts_db['post1'] = post1
	post2 = Post.create_post('username2', 'content2')
	posts_db['post2'] = post2
	search = Search({}, posts_db)
	assert search.search_posts('content1') == [post1]


def test_filter_posts():
	posts_db = {}
	post1 = Post.create_post('username1', '#content1')
	posts_db['post1'] = post1
	post2 = Post.create_post('username2', '@content2')
	posts_db['post2'] = post2
	search = Search({}, posts_db)
	assert search.filter_posts('hashtag', '#content1') == [post1]
	assert search.filter_posts('user_mention', '@content2') == [post2]
	assert search.filter_posts('trending_topic', '#content1') == [post1]
	assert search.filter_posts('invalid', '#content1') == 'Invalid filter type'
