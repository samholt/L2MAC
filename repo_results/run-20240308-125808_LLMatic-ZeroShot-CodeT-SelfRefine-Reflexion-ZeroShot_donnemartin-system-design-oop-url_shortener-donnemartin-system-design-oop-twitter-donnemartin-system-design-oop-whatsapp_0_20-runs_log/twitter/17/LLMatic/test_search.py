import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('email', 'username', 'password', False), User('email2', 'username2', 'password2', False)]
	search = Search(users, [])
	assert search.search_users('username')[0].username == users[0].username


def test_search_posts():
	users = [User('email', 'username', 'password', False)]
	posts = [Post(users[0], 'content'), Post(users[0], 'content2')]
	search = Search(users, posts)
	assert search.search_posts('content')[0].content == posts[0].content


def test_filter_posts():
	users = [User('email', 'username', 'password', False)]
	posts = [Post(users[0], 'content #hashtag'), Post(users[0], 'content2 @username'), Post(users[0], 'content3 #trending_topic'), Post(users[0], 'content4 #trending_topic')]
	search = Search(users, posts)
	assert search.filter_posts('hashtag', 'hashtag')[0].content == posts[0].content
	assert search.filter_posts('user_mention', 'username')[0].content == posts[1].content
	assert search.filter_posts('hashtag', 'trending_topic') == [posts[2], posts[3]]
