import pytest
from app import app, users, messages

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

def test_app_route():
	with app.test_client() as c:
		resp = c.get('/app')
		assert resp.status_code == 200
		assert resp.data == b'Welcome to the App!'

def test_users():
	assert isinstance(users, dict)

def test_messages():
	assert isinstance(messages, dict)

def test_signup():
	with app.test_client() as c:
		resp = c.post('/signup', json={
			'email': 'test@test.com', 
			'password': 'test123',
			'profile_picture': 'test.jpg',
			'status_message': 'Hello, world!',
			'privacy_settings': 'Public'
		})
		assert resp.status_code == 201
		assert users['test@test.com'] == {
			'password': 'test123',
			'profile_picture': 'test.jpg',
			'status_message': 'Hello, world!',
			'privacy_settings': 'Public',
			'blocked_contacts': [],
			'groups': {},
			'statuses': []
		}
		resp = c.post('/signup', json={
			'email': 'contact@test.com', 
			'password': 'test123',
			'profile_picture': 'test.jpg',
			'status_message': 'Hello, world!',
			'privacy_settings': 'Public'
		})
		assert resp.status_code == 201
		assert users['contact@test.com'] == {
			'password': 'test123',
			'profile_picture': 'test.jpg',
			'status_message': 'Hello, world!',
			'privacy_settings': 'Public',
			'blocked_contacts': [],
			'groups': {},
			'statuses': []
		}

def test_update_profile():
	with app.test_client() as c:
		resp = c.post('/update_profile', json={
			'email': 'test@test.com', 
			'profile_picture': 'test2.jpg',
			'status_message': 'Hello, world! Updated',
			'privacy_settings': 'Private'
		})
		assert resp.status_code == 200
		assert users['test@test.com'] == {
			'password': 'test123',
			'profile_picture': 'test2.jpg',
			'status_message': 'Hello, world! Updated',
			'privacy_settings': 'Private',
			'blocked_contacts': [],
			'groups': {},
			'statuses': []
		}

def test_post_status():
	with app.test_client() as c:
		resp = c.post('/post_status', json={'email': 'test@test.com', 'status': 'Hello, world! Status'})
		assert resp.status_code == 200
		assert 'Hello, world! Status' in users['test@test.com']['statuses']

def test_get_statuses():
	with app.test_client() as c:
		resp = c.get('/get_statuses', query_string={'email': 'test@test.com'})
		assert resp.status_code == 200
		assert resp.get_json() == ['Hello, world! Status']

def test_block_contact():
	with app.test_client() as c:
		resp = c.post('/block_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' in users['test@test.com']['blocked_contacts']

def test_unblock_contact():
	with app.test_client() as c:
		resp = c.post('/unblock_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' not in users['test@test.com']['blocked_contacts']

def test_create_group():
	with app.test_client() as c:
		resp = c.post('/create_group', json={'email': 'test@test.com', 'group_name': 'Test Group'})
		assert resp.status_code == 200
		assert 'Test Group' in users['test@test.com']['groups']

def test_edit_group():
	with app.test_client() as c:
		resp = c.post('/edit_group', json={'email': 'test@test.com', 'group_name': 'Test Group', 'new_group_name': 'New Test Group'})
		assert resp.status_code == 200
		assert 'Test Group' not in users['test@test.com']['groups']
		assert 'New Test Group' in users['test@test.com']['groups']

def test_manage_group():
	with app.test_client() as c:
		resp = c.post('/manage_group', json={'email': 'test@test.com', 'group_name': 'New Test Group', 'action': 'add', 'contact_email': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' in users['test@test.com']['groups']['New Test Group']
		resp = c.post('/manage_group', json={'email': 'test@test.com', 'group_name': 'New Test Group', 'action': 'remove', 'contact_email': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' not in users['test@test.com']['groups']['New Test Group']

def test_send_message():
	with app.test_client() as c:
		resp = c.post('/send_message', json={'sender_email': 'test@test.com', 'recipient_email': 'contact@test.com', 'message': 'Hello, contact!'})
		assert resp.status_code == 200
		assert messages['test@test.com']['contact@test.com'] == 'Hello, contact!'

def test_get_messages():
	with app.test_client() as c:
		resp = c.get('/get_messages', query_string={'email': 'contact@test.com'})
		assert resp.status_code == 200
		assert resp.get_json() == {'test@test.com': 'Hello, contact!'}

def test_recover():
	with app.test_client() as c:
		resp = c.post('/recover', json={'email': 'test@test.com'})
		assert resp.status_code == 200
		assert resp.get_json()['password'] == 'test123'
