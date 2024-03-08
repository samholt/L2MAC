import pytest
from app import app, users, offline_messages

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert b'Welcome to the Chat App!' in resp.data

def test_signup():
	with app.test_client() as c:
		resp = c.post('/signup', data={'email': 'test1@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert users['test1@test.com']['password'] == 'test123'
		resp = c.post('/signup', data={'email': 'test2@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert users['test2@test.com']['password'] == 'test123'
		resp = c.post('/signup', data={'email': 'test3@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert users['test3@test.com']['password'] == 'test123'

def test_update_status():
	with app.test_client() as c:
		resp = c.post('/update_status', data={'user_email': 'test1@test.com', 'status': 'online'})
		assert resp.status_code == 200
		assert users['test1@test.com']['online'] == True
		resp = c.post('/update_status', data={'user_email': 'test1@test.com', 'status': 'offline'})
		assert resp.status_code == 200
		assert users['test1@test.com']['online'] == False

def test_post_message():
	with app.test_client() as c:
		resp = c.post('/post_message', data={'user_email': 'test1@test.com', 'recipient_email': 'test2@test.com', 'message': 'Hello, world!'})
		assert resp.status_code == 200
		assert 'Hello, world!' in offline_messages['test2@test.com']
		resp = c.post('/update_status', data={'user_email': 'test2@test.com', 'status': 'online'})
		assert resp.status_code == 200
		assert 'Hello, world!' in users['test2@test.com']['messages']
		assert 'test2@test.com' not in offline_messages

