import pytest
import app
from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status


def test_register():
	with app.app.test_client() as c:
		response = c.post('/register', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 201


def test_login():
	with app.app.test_client() as c:
		response = c.post('/login', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200


def test_logout():
	with app.app.test_client() as c:
		response = c.post('/logout', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200


def test_profile():
	with app.app.test_client() as c:
		response = c.get('/profile', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200
		response = c.put('/profile', json={'email': 'test@test.com', 'password': 'test', 'picture': 'test.jpg', 'message': 'Hello, world!', 'settings': {'show_details': True, 'show_last_seen': True}})
		assert response.status_code == 200


def test_block():
	with app.app.test_client() as c:
		response = c.post('/block', json={'email': 'test@test.com', 'password': 'test', 'block_email': 'block@test.com', 'block_password': 'block'})
		assert response.status_code == 200


def test_unblock():
	with app.app.test_client() as c:
		response = c.post('/unblock', json={'email': 'test@test.com', 'password': 'test', 'unblock_email': 'unblock@test.com', 'unblock_password': 'unblock'})
		assert response.status_code == 200


def test_group():
	with app.app.test_client() as c:
		response = c.post('/group', json={'email': 'test@test.com', 'password': 'test', 'name': 'Test Group', 'picture': 'group.jpg', 'admins': ['admin@test.com']})
		assert response.status_code == 201
		response = c.put('/group', json={'email': 'test@test.com', 'password': 'test', 'name': 'Test Group', 'picture': 'group.jpg', 'admins': ['admin@test.com'], 'new_name': 'New Test Group', 'new_picture': 'new_group.jpg', 'new_admins': ['new_admin@test.com']})
		assert response.status_code == 200
		response = c.delete('/group', json={'email': 'test@test.com', 'password': 'test', 'name': 'New Test Group', 'picture': 'new_group.jpg', 'admins': ['new_admin@test.com']})
		assert response.status_code == 200


def test_message():
	with app.app.test_client() as c:
		response = c.post('/message', json={'sender_email': 'sender@test.com', 'sender_password': 'sender', 'receiver_email': 'receiver@test.com', 'receiver_password': 'receiver', 'content': 'Hello, world!'})
		assert response.status_code == 201
		response = c.put('/message', json={'sender_email': 'sender@test.com', 'sender_password': 'sender', 'receiver_email': 'receiver@test.com', 'receiver_password': 'receiver', 'content': 'Hello, world!'})
		assert response.status_code == 200


def test_status():
	with app.app.test_client() as c:
		response = c.post('/status', json={'email': 'test@test.com', 'password': 'test', 'content': 'Hello, world!', 'visibility': ['viewer@test.com'], 'expiry': '2022-12-31T23:59:59Z'})
		assert response.status_code == 201
		response = c.get('/status', json={'email': 'test@test.com', 'password': 'test', 'viewer_email': 'viewer@test.com', 'viewer_password': 'viewer'})
		assert response.status_code == 200
		response = c.delete('/status', json={'email': 'test@test.com', 'password': 'test', 'content': 'Hello, world!', 'visibility': ['viewer@test.com'], 'expiry': '2022-12-31T23:59:59Z'})
		assert response.status_code == 200

