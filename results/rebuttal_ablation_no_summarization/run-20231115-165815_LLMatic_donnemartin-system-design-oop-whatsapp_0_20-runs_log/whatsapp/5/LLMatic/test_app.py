import pytest
from app import app, users
import time

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Welcome to the User Management System!'

def test_users():
	assert isinstance(users, dict)
	assert len(users) == 0

def test_signup():
	with app.test_client() as c:
		resp = c.post('/signup', json={'email': 'test@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert users['test@test.com'] == {'password': 'test123', 'blocked': [], 'groups': {}, 'messages': [], 'read_receipts': {}, 'statuses': [], 'online': False, 'queued_messages': []}

def test_online():
	with app.test_client() as c:
		resp = c.post('/online', json={'email': 'test@test.com', 'online': True})
		assert resp.status_code == 200
		assert users['test@test.com']['online'] == True
		resp = c.post('/online', json={'email': 'test@test.com', 'online': False})
		assert resp.status_code == 200
		assert users['test@test.com']['online'] == False

def test_send_message():
	with app.test_client() as c:
		resp = c.post('/signup', json={'email': 'sender@test.com', 'password': 'sender123'})
		assert resp.status_code == 201
		resp = c.post('/send_message', json={'sender_email': 'sender@test.com', 'recipient_email': 'test@test.com', 'message': 'Hello'})
		assert resp.status_code == 200
		assert users['test@test.com']['queued_messages'] == [{'sender': 'sender@test.com', 'message': 'Hello'}]
		resp = c.post('/online', json={'email': 'test@test.com', 'online': True})
		assert resp.status_code == 200
		assert users['test@test.com']['messages'] == [{'sender': 'sender@test.com', 'message': 'Hello'}]
		assert users['test@test.com']['queued_messages'] == []

# Rest of the code...
