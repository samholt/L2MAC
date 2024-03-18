import pytest
from flask import Flask, json
import app

def test_get_users():
	app.users = {'1': {'email': 'test@test.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': [], 'messages': [], 'images': [], 'statuses': []}}
	with app.app.test_request_context():
		response = app.get_users()
	assert response.status_code == 200
	assert response.get_json() == app.users

def test_signup():
	with app.app.test_request_context('/signup', method='POST', data=json.dumps({'email': 'test2@test.com', 'password': 'password2'}), content_type='application/json'):
		response = app.signup()
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully', 'user_id': '2'}

def test_password_recovery():
	with app.app.test_request_context('/password_recovery/1'):
		response = app.password_recovery('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset link sent'}

def test_set_profile_picture():
	with app.app.test_request_context('/set_profile_picture/1', method='POST', data=json.dumps({'new_picture': 'new_picture.jpg'}), content_type='application/json'):
		response = app.set_profile_picture('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated'}
	assert app.users['1']['profile_picture'] == 'new_picture.jpg'

def test_set_status_message():
	with app.app.test_request_context('/set_status_message/1', method='POST', data=json.dumps({'new_message': 'Hello, world!'}), content_type='application/json'):
		response = app.set_status_message('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message updated'}
	assert app.users['1']['status_message'] == 'Hello, world!'

def test_update_privacy_settings():
	with app.app.test_request_context('/update_privacy_settings/1', method='POST', data=json.dumps({'new_settings': {'last_seen': 'nobody', 'profile_picture': 'friends', 'status_message': 'nobody'}}), content_type='application/json'):
		response = app.update_privacy_settings('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings updated'}
	assert app.users['1']['privacy_settings'] == {'last_seen': 'nobody', 'profile_picture': 'friends', 'status_message': 'nobody'}

def test_block_contact():
	with app.app.test_request_context('/block_contact/1', method='POST', data=json.dumps({'contact_id': '2'}), content_type='application/json'):
		response = app.block_contact('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked'}
	assert '2' in app.users['1']['blocked_contacts']

def test_unblock_contact():
	with app.app.test_request_context('/unblock_contact/1', method='POST', data=json.dumps({'contact_id': '2'}), content_type='application/json'):
		response = app.unblock_contact('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked'}
	assert '2' not in app.users['1']['blocked_contacts']

def test_manage_group():
	with app.app.test_request_context('/manage_group/1', method='POST', data=json.dumps({'group_details': {'group_id': '1', 'group_name': 'Friends', 'members': ['2', '3']}}), content_type='application/json'):
		response = app.manage_group('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group managed'}
	assert {'group_id': '1', 'group_name': 'Friends', 'members': ['2', '3']} in app.users['1']['groups']

def test_send_message():
	with app.app.test_request_context('/send_message/1', method='POST', data=json.dumps({'recipient_id': '2', 'message': 'Hello, world!'}), content_type='application/json'):
		response = app.send_message('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent', 'message_id': '1'}
	assert {'message_id': '1', 'message': 'Hello, world!', 'recipient_id': '2', 'read': False} in app.users['1']['messages']

def test_read_message():
	with app.app.test_request_context('/read_message/1', method='POST', data=json.dumps({'message_id': '1'}), content_type='application/json'):
		response = app.read_message('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message marked as read'}
	for message in app.users['1']['messages']:
		if message['message_id'] == '1':
			assert message['read'] == True
			break

def test_share_image():
	with app.app.test_request_context('/share_image/1', method='POST', data=json.dumps({'recipient_id': '2', 'image': 'image.jpg'}), content_type='application/json'):
		response = app.share_image('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Image shared', 'image_id': '1'}
	assert {'image_id': '1', 'image': 'image.jpg', 'recipient_id': '2'} in app.users['1']['images']

def test_post_status():
	with app.app.test_request_context('/post_status/1', method='POST', data=json.dumps({'status_details': {'text': 'Hello, world!', 'image': 'image.jpg', 'visibility': 'public'}}), content_type='application/json'):
		response = app.post_status('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status posted', 'status_id': '1'}
	assert {'status_id': '1', 'status_details': {'text': 'Hello, world!', 'image': 'image.jpg', 'visibility': 'public'}} in app.users['1']['statuses']

def test_update_status_visibility():
	with app.app.test_request_context('/update_status_visibility/1', method='POST', data=json.dumps({'status_id': '1', 'visibility': 'friends'}), content_type='application/json'):
		response = app.update_status_visibility('1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status visibility updated'}
	for status in app.users['1']['statuses']:
		if status['status_id'] == '1':
			assert status['status_details']['visibility'] == 'friends'
			break

