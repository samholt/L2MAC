import pytest
from user import User
from post import Post
from search import Search


def test_search():
	user1 = User('test1@test.com', 'test1', 'password1', False)
	user2 = User('test2@test.com', 'test2', 'password2', False)
	post1 = Post(user1, 'Hello world! #greetings')
	post2 = Post(user2, 'Goodbye world! @test1')
	search = Search([user1, user2], [post1, post2])

	user_results, post_results = search.search('world')
	assert user_results == []
	assert post_results == [post1, post2]

	user_results, post_results = search.search('test1')
	assert user_results == [user1]
	assert post_results == [post2]


def test_filter():
	user1 = User('test1@test.com', 'test1', 'password1', False)
	user2 = User('test2@test.com', 'test2', 'password2', False)
	post1 = Post(user1, 'Hello world! #greetings')
	post2 = Post(user2, 'Goodbye world! @test1')
	search = Search([user1, user2], [post1, post2])

	results = search.filter('hashtag', 'greetings')
	assert results == [post1]

	results = search.filter('user_mention', 'test1')
	assert results == [post2]

	results = search.filter('trending_topic', 'world')
	assert results == [post1, post2]

	results = search.filter('invalid', 'test')
	assert results == []
