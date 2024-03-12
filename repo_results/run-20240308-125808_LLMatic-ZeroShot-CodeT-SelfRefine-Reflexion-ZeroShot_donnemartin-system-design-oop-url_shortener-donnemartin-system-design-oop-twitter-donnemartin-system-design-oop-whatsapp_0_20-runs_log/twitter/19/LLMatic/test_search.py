import pytest
from user import User
from post import Post
from search import Search


def test_search_by_keyword():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'password', False)
	user1.register(users_db)
	user2 = User('test2@test.com', 'testuser2', 'password', False)
	user2.register(users_db)

	posts_db = {}
	post1 = Post(user1, 'This is a test post')
	post1.create()
	posts_db[post1.timestamp] = post1
	post2 = Post(user2, 'Another test post')
	post2.create()
	posts_db[post2.timestamp] = post2

	search = Search(users_db, posts_db)
	matched_users, matched_posts = search.search_by_keyword('test')
	assert len(matched_users) == 2
	assert len(matched_posts) == 2


def test_filter_posts():
	users_db = {}
	user1 = User('test1@test.com', 'testuser1', 'password', False)
	user1.register(users_db)

	posts_db = {}
	post1 = Post(user1, 'This is a #test post')
	post1.create()
	posts_db[post1.timestamp] = post1
	post2 = Post(user1, 'Another test post')
	post2.create()
	posts_db[post2.timestamp] = post2

	search = Search(users_db, posts_db)
	filtered_posts = search.filter_posts('hashtags')
	assert len(filtered_posts) == 1
	assert filtered_posts[0] == post1
