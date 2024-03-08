import pytest
from webapp import app


def test_home():
	with app.test_client() as c:
		response = c.get('/')
		assert response.status_code == 200
		assert b'Welcome to the Chat App' in response.data


def test_login():
	with app.test_client() as c:
		response = c.post('/login', data={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 200
		assert b'Login Failed' in response.data


def test_register():
	with app.test_client() as c:
		response = c.post('/register', data={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 200
		assert b'Registration Successful' in response.data


def test_send_message():
	with app.test_client() as c:
		response = c.post('/send_message', data={'message': 'Hello', 'recipient': 'test_recipient', 'username': 'test_user'})
		assert response.status_code == 200
		assert b'Message Sent' in response.data


def test_create_group():
	with app.test_client() as c:
		response = c.post('/create_group', data={'group_name': 'test_group', 'username': 'test_user'})
		assert response.status_code == 200
		assert b'Group Created' in response.data


def test_update_status():
	with app.test_client() as c:
		response = c.post('/update_status', data={'new_status': 'Online', 'username': 'test_user'})
		assert response.status_code == 200
		assert b'Status Updated' in response.data
