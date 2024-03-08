import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('email1', 'user1', 'pass1', False), User('email2', 'user2', 'pass2', False)]
	search = Search(users, [])
	assert search.search_users('user1') == [users[0]]
	assert search.search_users('user3') == []


def test_search_posts():
	users = [User('email1', 'user1', 'pass1', False)]
	posts = [Post(users[0], 'content1'), Post(users[0], 'content2')]
	search = Search(users, posts)
	assert search.search_posts('content1') == [posts[0]]
	assert search.search_posts('content3') == []


def test_filter_posts():
	users = [User('email1', 'user1', 'pass1', False)]
	posts = [Post(users[0], 'content1 #hashtag'), Post(users[0], '@user2 content2')]
	search = Search(users, posts)
	assert search.filter_posts('hashtag', 'hashtag') == [posts[0]]
	assert search.filter_posts('user_mention', 'user2') == [posts[1]]
	assert search.filter_posts('trending_topic', 'content1') == [posts[0]]
	assert search.filter_posts('invalid', 'value') == 'Invalid filter type'
