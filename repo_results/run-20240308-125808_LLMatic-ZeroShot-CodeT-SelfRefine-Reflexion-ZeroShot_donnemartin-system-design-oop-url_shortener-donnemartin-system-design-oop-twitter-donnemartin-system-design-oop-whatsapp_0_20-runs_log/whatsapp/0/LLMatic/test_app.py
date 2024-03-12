import pytest
from app import app, users, groups, messages, queue

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert b'Chat Application' in resp.data

def test_update_status():
	with app.test_client() as c:
		# Test updating status of non-existent user
		resp = c.post('/user/nonexistentuser/status', json={'status': 'online'})
		assert resp.status_code == 404
		# Test updating status of existing user
		users['testuser'] = {'online': 'offline'}
		resp = c.post('/user/testuser/status', json={'status': 'online'})
		assert resp.status_code == 200
		assert users['testuser']['online'] == 'online'

def test_send_message():
	with app.test_client() as c:
		# Test sending message to non-existent user
		resp = c.post('/message', json={'message': 'Hello', 'receiver': 'nonexistentuser'})
		assert resp.status_code == 404
		# Test sending message to offline user
		users['testuser'] = {'online': 'offline'}
		resp = c.post('/message', json={'message': 'Hello', 'receiver': 'testuser'})
		assert resp.status_code == 200
		assert queue['testuser'] == ['Hello']
		# Test sending message to online user
		users['testuser']['online'] = 'online'
		resp = c.post('/message', json={'message': 'Hello', 'receiver': 'testuser'})
		assert resp.status_code == 200
		assert messages['testuser'] == ['Hello']
		assert 'testuser' not in queue
		# Test sending message to online user and check if the message is removed from queue
		queue['testuser'] = ['Hello']
		resp = c.post('/message', json={'message': 'Hello', 'receiver': 'testuser'})
		assert resp.status_code == 200
		assert messages['testuser'] == ['Hello', 'Hello']
		assert 'testuser' not in queue
