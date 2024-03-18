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
		resp = c.post('/signup', data={'email': 'test@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert resp.data == b'User created successfully'
		assert 'test@test.com' in users
		assert users['test@test.com']['password'] == 'test123'

def test_recover():
	with app.test_client() as c:
		resp = c.get('/recover?email=test@test.com')
		assert resp.status_code == 200
		assert resp.data == b'test123'

def test_set_profile_picture():
	with app.test_client() as c:
		resp = c.post('/set_profile_picture', data={'email': 'test@test.com', 'profile_picture': 'picture.jpg'})
		assert resp.status_code == 200
		assert resp.data == b'Profile picture updated successfully'
		assert users['test@test.com']['profile_picture'] == 'picture.jpg'

def test_set_status_message():
	with app.test_client() as c:
		resp = c.post('/set_status_message', data={'email': 'test@test.com', 'status_message': 'Hello, world!'})
		assert resp.status_code == 200
		assert resp.data == b'Status message updated successfully'
		assert users['test@test.com']['status_message'] == 'Hello, world!'

def test_set_privacy_settings():
	with app.test_client() as c:
		resp = c.post('/set_privacy_settings', data={'email': 'test@test.com', 'privacy_settings': 'private'})
		assert resp.status_code == 200
		assert resp.data == b'Privacy settings updated successfully'
		assert users['test@test.com']['privacy_settings'] == 'private'

def test_block():
	with app.test_client() as c:
		resp = c.post('/block', data={'email': 'test@test.com', 'block_email': 'block@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'User blocked successfully'
		assert 'block@test.com' in users['test@test.com']['blocked']

def test_unblock():
	with app.test_client() as c:
		resp = c.post('/unblock', data={'email': 'test@test.com', 'unblock_email': 'block@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'User unblocked successfully'
		assert 'block@test.com' not in users['test@test.com']['blocked']

def test_create_group():
	with app.test_client() as c:
		resp = c.post('/create_group', data={'email': 'test@test.com', 'group_name': 'group1'})
		assert resp.status_code == 200
		assert resp.data == b'Group created successfully'
		assert 'group1' in users['test@test.com']['groups']

def test_edit_group():
	with app.test_client() as c:
		resp = c.post('/edit_group', data={'email': 'test@test.com', 'group_name': 'group1', 'new_group_name': 'group2'})
		assert resp.status_code == 200
		assert resp.data == b'Group edited successfully'
		assert 'group1' not in users['test@test.com']['groups']
		assert 'group2' in users['test@test.com']['groups']

def test_manage_group():
	with app.test_client() as c:
		resp = c.post('/manage_group', data={'email': 'test@test.com', 'group_name': 'group2', 'action': 'add', 'member_email': 'member@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'Member added to group successfully'
		assert 'member@test.com' in users['test@test.com']['groups']['group2']
		resp = c.post('/manage_group', data={'email': 'test@test.com', 'group_name': 'group2', 'action': 'remove', 'member_email': 'member@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'Member removed from group successfully'
		assert 'member@test.com' not in users['test@test.com']['groups']['group2']

def test_send_message():
	with app.test_client() as c:
		resp = c.post('/signup', data={'email': 'test2@test.com', 'password': 'test123'})
		assert resp.status_code == 201
		assert resp.data == b'User created successfully'
		assert 'test2@test.com' in users
		assert users['test2@test.com']['password'] == 'test123'
		resp = c.post('/send_message', data={'sender_email': 'test@test.com', 'receiver_email': 'test2@test.com', 'message': 'Hello, world!'})
		assert resp.status_code == 200
		assert resp.data == b'Message sent successfully'
		assert users['test@test.com']['messages'][-1]['to'] == 'test2@test.com'
		assert users['test@test.com']['messages'][-1]['message'] == 'Hello, world!'
		assert not users['test@test.com']['messages'][-1]['read']
		assert users['test2@test.com']['messages'][-1]['from'] == 'test@test.com'
		assert users['test2@test.com']['messages'][-1]['message'] == 'Hello, world!'
		assert not users['test2@test.com']['messages'][-1]['read']

def test_read_message():
	with app.test_client() as c:
		resp = c.post('/read_message', data={'email': 'test2@test.com', 'message_index': '0'})
		assert resp.status_code == 200
		assert resp.data == b'Message marked as read'
		assert users['test2@test.com']['messages'][0]['read']

def test_post_status():
	with app.test_client() as c:
		resp = c.post('/post_status', data={'email': 'test@test.com', 'status_image': 'status.jpg'})
		assert resp.status_code == 200
		assert resp.data == b'Status posted successfully'
		assert users['test@test.com']['status']['image'] == 'status.jpg'
		assert time.time() - users['test@test.com']['status']['timestamp'] < 1

def test_view_status():
	with app.test_client() as c:
		time.sleep(1)
		resp = c.get('/view_status?email=test@test.com&viewer_email=test2@test.com')
		assert resp.status_code == 200
		assert resp.data == b'status.jpg'
		resp = c.post('/set_privacy_settings', data={'email': 'test@test.com', 'privacy_settings': 'private'})
		assert resp.status_code == 200
		assert resp.data == b'Privacy settings updated successfully'
		assert users['test@test.com']['privacy_settings'] == 'private'
		resp = c.get('/view_status?email=test@test.com&viewer_email=test2@test.com')
		assert resp.status_code == 404
		assert resp.data == b'User not found, blocked, or private'
		resp = c.post('/manage_group', data={'email': 'test@test.com', 'group_name': 'group2', 'action': 'add', 'member_email': 'test2@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'Member added to group successfully'
		assert 'test2@test.com' in users['test@test.com']['groups']['group2']
		resp = c.get('/view_status?email=test@test.com&viewer_email=test2@test.com')
		assert resp.status_code == 200
		assert resp.data == b'status.jpg'
		time.sleep(1)
		resp = c.get('/view_status?email=test@test.com&viewer_email=test2@test.com')
		assert resp.status_code == 404
		assert resp.data == b'No status found'

