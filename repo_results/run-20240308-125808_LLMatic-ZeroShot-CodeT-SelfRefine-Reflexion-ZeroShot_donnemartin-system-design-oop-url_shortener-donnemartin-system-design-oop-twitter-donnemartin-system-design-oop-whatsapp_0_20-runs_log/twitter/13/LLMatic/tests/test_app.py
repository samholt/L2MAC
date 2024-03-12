import pytest
import app
import jwt
from flask import Flask


def test_trending():
	app.posts_db = {
		0: app.Post('user1', '#topic1 #topic2', 0),
		1: app.Post('user2', '#topic2 #topic3', 1),
		2: app.Post('user3', '#topic1 #topic3', 2),
		3: app.Post('user4', '#topic1 #topic2 #topic3', 3)
	}

	with app.app.test_client() as c:
		response = c.get('/trending')
	trending = response.get_json()['trending']

	assert len(trending) == 3
	assert trending[0] == ['#topic1', 3]
	assert trending[1] == ['#topic2', 3]
	assert trending[2] == ['#topic3', 3]


def test_trending_with_no_posts():
	app.posts_db = {}

	with app.app.test_client() as c:
		response = c.get('/trending')
	trending = response.get_json()['trending']

	assert len(trending) == 0


def test_trending_with_no_hashtags():
	app.posts_db = {
		0: app.Post('user1', 'Hello world', 0),
		1: app.Post('user2', 'Another post', 1),
		2: app.Post('user3', 'Yet another post', 2),
		3: app.Post('user4', 'This is a post', 3)
	}

	with app.app.test_client() as c:
		response = c.get('/trending')
	trending = response.get_json()['trending']

	assert len(trending) == 0


def test_recommendations():
	app.users_db = {
		'user1': app.User('email1', 'user1', 'password1', followers=['user2', 'user3', 'user4']),
		'user2': app.User('email2', 'user2', 'password2', followers=['user1', 'user3']),
		'user3': app.User('email3', 'user3', 'password3', followers=['user1', 'user2']),
		'user4': app.User('email4', 'user4', 'password4', followers=['user1'])
	}

	token = jwt.encode({'username': 'user1'}, 'secret', algorithm='HS256')

	with app.app.test_client() as c:
		response = c.get('/recommendations', headers={'Authorization': token})
	recommendations = response.get_json()['recommendations']

	assert len(recommendations) == 4
	assert recommendations[0]['username'] == 'user2'
	assert recommendations[1]['username'] == 'user3'
	assert recommendations[2]['username'] == 'user4'


def test_recommendations_with_no_users():
	app.users_db = {}

	token = jwt.encode({'username': 'user1'}, 'secret', algorithm='HS256')

	with app.app.test_client() as c:
		response = c.get('/recommendations', headers={'Authorization': token})
	recommendations = response.get_json()['recommendations']

	assert len(recommendations) == 0



