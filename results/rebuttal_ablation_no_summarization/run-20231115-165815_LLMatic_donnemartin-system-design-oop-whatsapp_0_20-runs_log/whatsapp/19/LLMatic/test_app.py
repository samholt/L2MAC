import pytest
import app
from flask import Flask

def test_get_users():
	app.users = {'1': {'email': 'test@test.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': []}}
	with app.app.test_request_context():
		response = app.get_users()
		assert response.status_code == 200
		assert response.get_json() == app.users

def test_signup():
	with app.app.test_request_context(json={'email': 'test2@test.com', 'password': 'password2'}):
		response = app.signup()
		assert response[1] == 201
		user_id = response[0].get_json().get('user_id')
		assert user_id in app.users

def test_forgot_password():
	with app.app.test_request_context(json={'user_id': '1'}):
		response = app.forgot_password()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Password reset link has been sent to your email.'
	with app.app.test_request_context(json={'user_id': '2'}):
		response = app.forgot_password()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

def test_set_profile_picture():
	with app.app.test_request_context(json={'user_id': '1', 'new_picture': 'new_picture.jpg'}):
		response = app.set_profile_picture()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Profile picture updated.'
		assert app.users['1']['profile_picture'] == 'new_picture.jpg'
	with app.app.test_request_context(json={'user_id': '2', 'new_picture': 'new_picture.jpg'}):
		response = app.set_profile_picture()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

def test_set_status_message():
	with app.app.test_request_context(json={'user_id': '1', 'new_message': 'Hello, world!'}):
		response = app.set_status_message()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Status message updated.'
		assert app.users['1']['status_message'] == 'Hello, world!'
	with app.app.test_request_context(json={'user_id': '2', 'new_message': 'Hello, world!'}):
		response = app.set_status_message()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

def test_update_privacy_settings():
	with app.app.test_request_context(json={'user_id': '1', 'new_settings': {'hide_profile_picture': True}}):
		response = app.update_privacy_settings()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Privacy settings updated.'
		assert app.users['1']['privacy_settings'] == {'hide_profile_picture': True}
	with app.app.test_request_context(json={'user_id': '2', 'new_settings': {'hide_profile_picture': True}}):
		response = app.update_privacy_settings()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

def test_block_contact():
	with app.app.test_request_context(json={'user_id': '1', 'contact_id': '2'}):
		response = app.block_contact()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Contact blocked.'
		assert '2' in app.users['1']['blocked_contacts']
	with app.app.test_request_context(json={'user_id': '2', 'contact_id': '1'}):
		response = app.block_contact()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

def test_unblock_contact():
	app.users['1']['blocked_contacts'].append('2')
	with app.app.test_request_context(json={'user_id': '1', 'contact_id': '2'}):
		response = app.unblock_contact()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Contact unblocked.'
		assert '2' not in app.users['1']['blocked_contacts']
	app.users['1']['blocked_contacts'].remove('2')
	with app.app.test_request_context(json={'user_id': '2', 'contact_id': '1'}):
		response = app.unblock_contact()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found or contact not blocked.'

def test_create_group():
	with app.app.test_request_context(json={'user_id': '1', 'group_details': {'name': 'Test Group', 'members': ['2', '3']}}):
		response = app.create_group()
		assert response[1] == 200
		assert response[0].get_json().get('message') == 'Group created.'
		assert {'name': 'Test Group', 'members': ['2', '3']} in app.users['1']['groups']
	with app.app.test_request_context(json={'user_id': '2', 'group_details': {'name': 'Test Group', 'members': ['1', '3']}}):
		response = app.create_group()
		assert response[1] == 404
		assert response[0].get_json().get('message') == 'User not found.'

