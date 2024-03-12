import pytest
from flask import Flask
import app

def test_home():
	with app.app.test_client() as c:
		response = c.get('/')
		assert response.status_code == 200
		assert b'Welcome to the Chat Application!' in response.data

def test_update_status():
	with app.app.test_client() as c:
		response = c.post('/status', json={'user_id': '1', 'status': 'online'})
		assert response.status_code == 200
		assert app.statuses['1'] == 'online'

def test_send_message():
	with app.app.test_client() as c:
		app.statuses['1'] = 'offline'
		response = c.post('/message', json={'receiver_id': '1', 'message': 'Hello'})
		assert response.status_code == 200
		assert app.queued_messages['1'] == ['Hello']
		app.statuses['1'] = 'online'
		response = c.post('/message', json={'receiver_id': '1', 'message': 'Hello'})
		assert response.status_code == 200
		assert app.messages['1'] == 'Hello'
