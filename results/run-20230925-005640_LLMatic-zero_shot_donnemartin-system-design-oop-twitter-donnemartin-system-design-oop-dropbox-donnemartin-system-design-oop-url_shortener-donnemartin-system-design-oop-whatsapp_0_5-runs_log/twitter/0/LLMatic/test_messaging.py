import pytest
from flask import Flask, request
from database import users_db, messages_db
from messaging import app


def test_message():
	app.config['TESTING'] = True
	client = app.test_client()

	# Add test users
	users_db['test1@example.com'] = {'email': 'test1@example.com', 'username': 'test1', 'password': 'password1'}
	users_db['test2@example.com'] = {'email': 'test2@example.com', 'username': 'test2', 'password': 'password2'}

	# Test sending message
	response = client.post('/message', headers={'Authorization': 'test1@example.com'}, json={'receiver_id': 'test2@example.com', 'content': 'Hello', 'timestamp': '2022-01-01T00:00:00Z', 'message_id': '1'})
	assert response.status_code == 201
	assert '1' in messages_db

	# Test blocking user
	response = client.post('/block', headers={'Authorization': 'test1@example.com'}, json={'blocked_user_email': 'test2@example.com'})
	assert response.status_code == 200
	assert 'test2@example.com' in users_db['test1@example.com']['blocked_users']

	# Test unblocking user
	response = client.post('/unblock', headers={'Authorization': 'test1@example.com'}, json={'unblocked_user_email': 'test2@example.com'})
	assert response.status_code == 200
	assert 'test2@example.com' not in users_db['test1@example.com']['blocked_users']

