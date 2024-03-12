import pytest
from app import app, users

def test_home():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200
		assert b'<!DOCTYPE html>' in response.data

def test_user_status():
	with app.test_client() as client:
		users['test_user'] = {'status': 'online', 'messages': []}
		response = client.get('/status/test_user')
		assert response.status_code == 200
		assert response.get_json() == {'status': 'online'}

def test_send_message():
	with app.test_client() as client:
		users['test_user'] = {'status': 'offline', 'messages': []}
		response = client.post('/message', json={'username': 'test_user', 'message': 'Hello'})
		assert response.status_code == 200
		assert response.get_json() == {'status': 'Message queued'}
		assert users['test_user']['messages'] == ['Hello']
