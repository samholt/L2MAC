import pytest
from app import app, User, Post
from flask import json


def test_get_trending_topics():
	user1 = User('test1@test.com', 'test1', 'password1')
	user2 = User('test2@test.com', 'test2', 'password2')
	user3 = User('test3@test.com', 'test3', 'password3')
	user4 = User('test4@test.com', 'test4', 'password4')
	user5 = User('test5@test.com', 'test5', 'password5')

	app.users_db = {
		'test1@test.com': user1,
		'test2@test.com': user2,
		'test3@test.com': user3,
		'test4@test.com': user4,
		'test5@test.com': user5
	}

	post1 = Post(user1, '#test1 #test2', ['#test1', '#test2'])
	post2 = Post(user2, '#test2 #test3', ['#test2', '#test3'])
	post3 = Post(user3, '#test3 #test1', ['#test3', '#test1'])
	post4 = Post(user4, '#test4 #test2', ['#test4', '#test2'])
	post5 = Post(user5, '#test5 #test3', ['#test5', '#test3'])

	app.posts_db = {
		1: post1,
		2: post2,
		3: post3,
		4: post4,
		5: post5
	}

	with app.test_client() as c:
		response = c.get('/get_trending_topics')

	assert json.loads(response.get_data()) == {'trending_topics': [('#test2', 3), ('#test1', 2), ('#test3', 2), ('#test4', 1), ('#test5', 1)]}


def test_recommend_users():
	user1 = User('test1@test.com', 'test1', 'password1')
	user2 = User('test2@test.com', 'test2', 'password2')
	user3 = User('test3@test.com', 'test3', 'password3')
	user4 = User('test4@test.com', 'test4', 'password4')
	user5 = User('test5@test.com', 'test5', 'password5')

	user1.follow(user2)
	user2.follow(user1)
	user2.follow(user3)
	user3.follow(user2)
	user3.follow(user4)
	user4.follow(user3)
	user4.follow(user5)
	user5.follow(user4)

	app.users_db = {
		'test1@test.com': user1,
		'test2@test.com': user2,
		'test3@test.com': user3,
		'test4@test.com': user4,
		'test5@test.com': user5
	}

	with app.test_client() as c:
		response = c.get('/recommend_users', query_string={'user_email': 'test1@test.com'})

	assert json.loads(response.get_data()) == {'recommended_users': [user3.__dict__, user4.__dict__, user5.__dict__]}
