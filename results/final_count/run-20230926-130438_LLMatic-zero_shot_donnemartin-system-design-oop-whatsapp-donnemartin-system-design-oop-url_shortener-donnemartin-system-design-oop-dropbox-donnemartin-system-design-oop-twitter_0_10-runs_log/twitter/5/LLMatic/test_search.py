import pytest
from user import User
from post import Post
from search import Search


def test_search_users():
	users = [User('email1', 'user1', 'pass1', False), User('email2', 'user2', 'pass2', False)]
	search = Search(users, [])
	assert search.search_users('user1') == [users[0]]


def test_search_posts():
	posts = [Post('user1', 'content1'), Post('user2', 'content2')]
	search = Search([], posts)
	assert search.search_posts('content1') == [posts[0]]


def test_filter_posts():
	posts = [Post('user1', '#content1'), Post('user2', '@content2'), Post('user3', 'trending_content')]
	search = Search([], posts)
	assert search.filter_posts('hashtag', 'content1') == [posts[0]]
	assert search.filter_posts('user_mention', 'content2') == [posts[1]]
	assert search.filter_posts('trending_topic', 'trending_content') == [posts[2]]
