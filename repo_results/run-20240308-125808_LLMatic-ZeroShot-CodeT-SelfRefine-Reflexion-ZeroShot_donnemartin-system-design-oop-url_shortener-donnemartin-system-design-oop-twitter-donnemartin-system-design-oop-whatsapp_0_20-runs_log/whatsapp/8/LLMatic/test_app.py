import pytest
from app import app, users

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

def test_webapp():
	with app.test_client() as c:
		resp = c.get('/webapp')
		assert resp.status_code == 200
		assert resp.data == b'Welcome to the web application!'

def test_status():
	with app.test_client() as c:
		resp = c.get('/status/testuser')
		assert resp.status_code == 404
		users['testuser'] = {'status': 'online', 'messages': []}
		resp = c.get('/status/testuser')
		assert resp.status_code == 200
		assert resp.json == {'status': 'online'}

def test_message():
	with app.test_client() as c:
		users['testuser'] = {'status': 'offline', 'messages': []}
		resp = c.post('/message/testuser', json={'message': 'Hello'})
		assert resp.status_code == 200
		assert resp.json == {'status': 'Message sent'}
		assert users['testuser']['messages'] == ['Hello']
