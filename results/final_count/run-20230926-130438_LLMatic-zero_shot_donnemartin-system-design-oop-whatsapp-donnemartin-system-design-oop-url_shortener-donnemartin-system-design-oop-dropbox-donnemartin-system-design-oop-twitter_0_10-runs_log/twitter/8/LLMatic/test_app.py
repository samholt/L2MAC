import pytest
import app
import json


def test_register():
	with app.app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		assert 'email' in json.loads(resp.data)
		assert 'username' in json.loads(resp.data)


def test_login():
	with app.app.test_client() as c:
		resp = c.post('/login', json={'username': 'test'})
		assert resp.status_code == 200
		assert 'token' in json.loads(resp.data)


def test_create_post():
	with app.app.test_client() as c:
		resp = c.post('/post', json={'user': 'test', 'text': 'Hello, World!'})
		assert resp.status_code == 201
		assert 'user' in json.loads(resp.data)


def test_search():
	with app.app.test_client() as c:
		resp = c.get('/search', json={'data': ['Hello, World!'], 'keyword': 'Hello'})
		assert resp.status_code == 200
		assert 'Hello, World!' in json.loads(resp.data)


def test_send_message():
	with app.app.test_client() as c:
		resp = c.post('/message', json={'sender': 'test', 'recipient': 'test2', 'text': 'Hello, World!'})
		assert resp.status_code == 200
		assert 'Message not sent. You are blocked by the recipient.' in json.loads(resp.data)


def test_send_notification():
	with app.app.test_client() as c:
		resp = c.post('/notification', json={'user': 'test', 'event': 'New follower'})
		assert resp.status_code == 200
		assert 'Notification for test: New follower' == json.loads(resp.data)


def test_trending():
	with app.app.test_client() as c:
		resp = c.get('/trending')
		assert resp.status_code == 200


def test_recommend():
	with app.app.test_client() as c:
		resp = c.get('/recommend', json={'user': 'test'})
		assert resp.status_code == 200
		assert 'test' not in json.loads(resp.data)

