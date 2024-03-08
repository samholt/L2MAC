import pytest
import app
from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status
from database import Database


def setup_function():
	user1 = User('test@test.com', 'test')
	user2 = User('contact@test.com', 'contact')
	Database.add_user(user1)
	Database.add_user(user2)


def test_signup():
	with app.app.test_client() as c:
		resp = c.post('/signup', json={'email': 'test2@test.com', 'password': 'test2'})
		assert resp.get_data() == b'User created successfully'


def test_recover_password():
	with app.app.test_client() as c:
		resp = c.post('/recover_password', json={'email': 'test@test.com'})
		assert resp.get_data() == b'Password recovery email sent'


def test_set_profile_picture():
	with app.app.test_client() as c:
		resp = c.post('/set_profile_picture', json={'email': 'test@test.com', 'picture': 'picture.jpg'})
		assert resp.get_data() == b'Profile picture updated'


def test_set_status_message():
	with app.app.test_client() as c:
		resp = c.post('/set_status_message', json={'email': 'test@test.com', 'message': 'Hello, world!'})
		assert resp.get_data() == b'Status message updated'


def test_set_privacy_settings():
	with app.app.test_client() as c:
		resp = c.post('/set_privacy_settings', json={'email': 'test@test.com', 'settings': 'Private'})
		assert resp.get_data() == b'Privacy settings updated'


def test_block_contact():
	with app.app.test_client() as c:
		resp = c.post('/block_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
		assert resp.get_data() == b'Contact blocked'


def test_unblock_contact():
	with app.app.test_client() as c:
		resp = c.post('/unblock_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
		assert resp.get_data() == b'Contact unblocked'


def test_send_message():
	with app.app.test_client() as c:
		resp = c.post('/send_message', json={'sender_email': 'test@test.com', 'receiver_email': 'contact@test.com', 'content': 'Hello, contact!'})
		assert resp.get_data() == b'Message sent'


def test_create_group():
	with app.app.test_client() as c:
		resp = c.post('/create_group', json={'name': 'Test Group', 'picture': 'group.jpg'})
		assert resp.get_data() == b'Group created'


def test_post_status():
	with app.app.test_client() as c:
		resp = c.post('/post_status', json={'email': 'test@test.com', 'content': 'Hello, world!', 'visibility': 'Public'})
		assert resp.get_data() == b'Status posted'

