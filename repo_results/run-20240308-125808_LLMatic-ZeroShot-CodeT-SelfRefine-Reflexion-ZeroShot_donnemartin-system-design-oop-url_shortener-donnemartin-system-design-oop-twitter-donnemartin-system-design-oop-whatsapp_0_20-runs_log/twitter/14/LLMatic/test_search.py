import pytest
from user import User, register, authenticate, mock_db as user_db
from post import Post, mock_db as post_db
from search import Search


def setup_module(module):
	user_db.clear()
	post_db.clear()
	register('test@test.com', 'testuser', 'password', False)
	Post.create(post_db, 'This is a test post #test', [], 'testuser')


def test_search_users():
	search = Search(user_db, post_db)
	assert search.search_users('testuser') == [user_db['testuser']]
	assert search.search_users('nonexistentuser') == []


def test_search_posts():
	search = Search(user_db, post_db)
	assert search.search_posts('#test') == [post for post in post_db.values() if '#test' in post.text]
	assert search.search_posts('#nonexistenthashtag') == []


def test_filter_posts():
	search = Search(user_db, post_db)
	assert search.filter_posts('hashtag', '#test') == [post for post in post_db.values() if '#test' in post.text.split()]
	assert search.filter_posts('user_mention', '@testuser') == []
	assert search.filter_posts('trending_topic', '') == sorted(post_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)[:10]
