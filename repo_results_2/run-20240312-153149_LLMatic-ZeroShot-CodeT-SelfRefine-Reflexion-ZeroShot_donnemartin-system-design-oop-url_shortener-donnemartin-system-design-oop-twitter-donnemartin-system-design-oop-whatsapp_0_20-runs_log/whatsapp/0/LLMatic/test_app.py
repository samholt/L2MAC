import pytest
from flask import Flask
import app as application

app = application.app


def test_home():
	with app.test_client() as c:
		response = c.get('/')
		assert response.status_code == 200
		assert b'Welcome to Chat App!' in response.data


def test_update_status():
	application.DATABASE['users']['test@example.com'] = {'status': 'offline'}
	with app.test_client() as c:
		response = c.post('/update_status', json={'email': 'test@example.com', 'status': 'online'})
		assert response.status_code == 200
		assert b'Status updated successfully' in response.data
		assert application.DATABASE['users']['test@example.com']['status'] == 'online'


def test_queue_message():
	with app.test_client() as c:
		response = c.post('/queue_message', json={'message': 'Hello, world!'})
		assert response.status_code == 200
		assert b'Message queued successfully' in response.data
		assert 'Hello, world!' in application.DATABASE['messages']
