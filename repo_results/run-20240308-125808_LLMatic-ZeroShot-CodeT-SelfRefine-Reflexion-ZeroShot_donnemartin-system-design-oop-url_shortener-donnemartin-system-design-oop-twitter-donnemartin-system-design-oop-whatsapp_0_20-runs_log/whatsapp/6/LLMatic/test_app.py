import pytest
from app import app, users, messages, statuses
import hashlib
import time

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

def test_users():
	assert isinstance(users, dict)

def test_signup():
	with app.test_client() as c:
		resp = c.post('/signup', json={'email': 'test@test.com', 'password': 'test'})
		assert resp.status_code == 201
		assert users['test@test.com']['password'] == 'test'

def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'email': 'test@test.com', 'password': 'test'})
		assert resp.status_code == 200

def test_recover():
	with app.test_client() as c:
		resp = c.post('/recover', json={'email': 'test@test.com'})
		assert resp.status_code == 200
		assert resp.data == b'test'

def test_set_profile_picture():
	with app.test_client() as c:
		resp = c.post('/set_profile_picture', json={'email': 'test@test.com', 'profile_picture': 'test.jpg'})
		assert resp.status_code == 200
		assert users['test@test.com']['profile_picture'] == 'test.jpg'

def test_set_status_message():
	with app.test_client() as c:
		resp = c.post('/set_status_message', json={'email': 'test@test.com', 'status_message': 'Hello, world!'})
		assert resp.status_code == 200
		assert users['test@test.com']['status_message'] == 'Hello, world!'

def test_update_privacy_settings():
	with app.test_client() as c:
		resp = c.post('/update_privacy_settings', json={'email': 'test@test.com', 'privacy_settings': {'details': False, 'last_seen': False}})
		assert resp.status_code == 200
		assert users['test@test.com']['privacy_settings'] == {'details': False, 'last_seen': False}

def test_block_contact():
	with app.test_client() as c:
		resp = c.post('/block_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' in users['test@test.com']['blocked_contacts']

def test_unblock_contact():
	with app.test_client() as c:
		resp = c.post('/unblock_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
		assert resp.status_code == 200
		assert 'contact@test.com' not in users['test@test.com']['blocked_contacts']

def test_create_group():
	with app.test_client() as c:
		resp = c.post('/create_group', json={'email': 'test@test.com', 'group_name': 'test_group'})
		assert resp.status_code == 201
		assert 'test_group' in users['test@test.com']['groups']

def test_add_participant():
	with app.test_client() as c:
		resp = c.post('/add_participant', json={'email': 'test@test.com', 'group_name': 'test_group', 'participant': 'participant@test.com'})
		assert resp.status_code == 200
		assert 'participant@test.com' in users['test@test.com']['groups']['test_group']['members']

def test_remove_participant():
	with app.test_client() as c:
		resp = c.post('/remove_participant', json={'email': 'test@test.com', 'group_name': 'test_group', 'participant': 'participant@test.com'})
		assert resp.status_code == 200
		assert 'participant@test.com' not in users['test@test.com']['groups']['test_group']['members']

def test_set_admin():
	with app.test_client() as c:
		resp = c.post('/set_admin', json={'email': 'test@test.com', 'group_name': 'test_group', 'admin': 'admin@test.com'})
		assert resp.status_code == 200
		assert 'admin@test.com' in users['test@test.com']['groups']['test_group']['admins']

def test_remove_admin():
	with app.test_client() as c:
		resp = c.post('/remove_admin', json={'email': 'test@test.com', 'group_name': 'test_group', 'admin': 'admin@test.com'})
		assert resp.status_code == 200
		assert 'admin@test.com' not in users['test@test.com']['groups']['test_group']['admins']

def test_send_message():
	with app.test_client() as c:
		resp = c.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'receiver@test.com', 'content': 'Hello, world!'})
		assert resp.status_code == 200
		conversation_id = hashlib.sha256(('test@test.com' + 'receiver@test.com').encode()).hexdigest()
		assert conversation_id in messages
		assert messages[conversation_id][-1]['content'] == 'Hello, world!'

def test_read_message():
	with app.test_client() as c:
		conversation_id = hashlib.sha256(('test@test.com' + 'receiver@test.com').encode()).hexdigest()
		resp = c.post('/read_message', json={'conversation_id': conversation_id, 'message_index': 0})
		assert resp.status_code == 200
		assert messages[conversation_id][0]['read']

def test_encrypt_message():
	with app.test_client() as c:
		conversation_id = hashlib.sha256(('test@test.com' + 'receiver@test.com').encode()).hexdigest()
		resp = c.post('/encrypt_message', json={'conversation_id': conversation_id, 'message_index': 0})
		assert resp.status_code == 200
		assert messages[conversation_id][0]['encrypted']
		assert messages[conversation_id][0]['content'] == hashlib.sha256('Hello, world!'.encode()).hexdigest()

def test_decrypt_message():
	with app.test_client() as c:
		conversation_id = hashlib.sha256(('test@test.com' + 'receiver@test.com').encode()).hexdigest()
		resp = c.post('/decrypt_message', json={'conversation_id': conversation_id, 'message_index': 0})
		assert resp.status_code == 400

def test_post_status():
	with app.test_client() as c:
		resp = c.post('/post_status', json={'email': 'test@test.com', 'image': 'status.jpg', 'visibility': 'public', 'expiry': 3600})
		assert resp.status_code == 200
		assert 'test@test.com' in statuses
		assert statuses['test@test.com'][-1]['image'] == 'status.jpg'
		assert statuses['test@test.com'][-1]['visibility'] == 'public'
		assert statuses['test@test.com'][-1]['expiry'] == 3600

def test_view_status():
	with app.test_client() as c:
		resp = c.post('/post_status', json={'email': 'test@test.com', 'image': 'status.jpg', 'visibility': ['viewer@test.com'], 'expiry': 3600})
		assert resp.status_code == 200
		resp = c.post('/view_status', json={'email': 'test@test.com', 'viewer': 'viewer@test.com'})
		assert resp.status_code == 200
		assert resp.get_json()['statuses'] == [status for status in statuses['test@test.com'] if status['visibility'] == 'public' or 'viewer@test.com' in status['visibility']]
