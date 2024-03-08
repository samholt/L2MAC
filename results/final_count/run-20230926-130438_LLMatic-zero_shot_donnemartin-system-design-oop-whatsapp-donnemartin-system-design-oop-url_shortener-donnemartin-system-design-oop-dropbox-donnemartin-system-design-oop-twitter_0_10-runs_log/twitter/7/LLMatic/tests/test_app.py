import pytest
from app import app, User, Post, users_db, posts_db


def setup_module(module):
	with app.app_context():
		user1 = User('test1@test.com', 'test1', 'test123')
		user2 = User('test2@test.com', 'test2', 'test123')
		user3 = User('test3@test.com', 'test3', 'test123')
		users_db[user1.username] = user1
		users_db[user2.username] = user2
		users_db[user3.username] = user3


def teardown_module(module):
	with app.app_context():
		users_db.clear()


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test4@test.com', 'username': 'test4', 'password': 'test123'})
		assert resp.status_code == 201
		assert resp.get_json() == {'message': 'User registered successfully'}


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test1', 'password': 'test123'})
		assert resp.status_code == 200
		assert 'token' in resp.get_json()


def test_follow():
	with app.test_client() as c:
		resp = c.post('/follow', json={'username': 'test1', 'password': 'test123', 'to_follow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Followed successfully'}


def test_unfollow():
	with app.test_client() as c:
		resp = c.post('/unfollow', json={'username': 'test1', 'password': 'test123', 'to_unfollow': 'test2'})
		assert resp.status_code == 200
		assert resp.get_json() == {'message': 'Unfollowed successfully'}


def test_post():
	with app.test_client() as c:
		resp = c.post('/create_post', json={'username': 'test1', 'password': 'test123', 'text': 'Hello, world!', 'images': []})
		assert resp.status_code == 201
		assert resp.get_json() == {'message': 'Post created successfully'}


def test_feed():
	with app.test_client() as c:
		resp = c.get('/timeline', query_string={'username': 'test1'})
		assert resp.status_code == 200
		assert 'timeline' in resp.get_json()


def test_notifications():
	with app.test_client() as c:
		resp = c.get('/notifications', query_string={'username': 'test1'})
		assert resp.status_code == 200
		assert 'notifications' in resp.get_json()


def test_recommendations():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test3@test.com', 'username': 'test3', 'password': 'test123'})
		resp = c.post('/follow', json={'username': 'test2', 'password': 'test123', 'to_follow': 'test3'})
		resp = c.get('/recommendations', query_string={'username': 'test1'})
		assert resp.status_code == 200
		assert 'recommendations' in resp.get_json()
