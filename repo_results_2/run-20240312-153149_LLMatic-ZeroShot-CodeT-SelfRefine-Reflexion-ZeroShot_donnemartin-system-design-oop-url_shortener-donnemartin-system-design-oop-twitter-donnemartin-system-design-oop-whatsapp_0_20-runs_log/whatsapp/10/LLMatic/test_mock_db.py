import pytest
import mock_db

db = mock_db.MockDB()

def setup_module(module):
	db.add_user('test_user', 'test_password')
	db.create_group('test_user', {'name': 'Test Group', 'picture': 'test_picture.jpg'})
	db.add_participant(1, 'test_user')
	db.add_admin(1, 'test_user')

def test_create_group():
	db.add_user('test_user2', 'test_password')
	db.create_group('test_user2', {'name': 'Test Group', 'picture': 'test_picture.jpg'})
	user = db.get_user('test_user2')
	assert user is not None
	assert user['groups'][1]['name'] == 'Test Group'

def test_edit_group():
	db.edit_group('test_user', 1, {'name': 'Edited Test Group', 'picture': 'edited_test_picture.jpg'})
	user = db.get_user('test_user')
	assert user is not None
	assert user['groups'][1]['name'] == 'Edited Test Group'

def test_delete_group():
	db.delete_group('test_user', 1)
	user = db.get_user('test_user')
	assert user is not None
	assert 1 not in user['groups']

def test_add_participant():
	db.add_user('test_user3', 'test_password')
	db.add_participant(1, 'test_user3')
	user = db.get_user('test_user')
	assert user is not None
	assert 'test_user3' in user['groups'][1]['participants']

def test_remove_participant():
	db.remove_participant(1, 'test_user3')
	user = db.get_user('test_user')
	assert user is not None
	assert 'test_user3' not in user['groups'][1]['participants']

def test_add_admin():
	db.add_user('test_user4', 'test_password')
	db.add_admin(1, 'test_user4')
	user = db.get_user('test_user')
	assert user is not None
	assert 'test_user4' in user['groups'][1]['admins']

def test_remove_admin():
	db.remove_admin(1, 'test_user4')
	user = db.get_user('test_user')
	assert user is not None
	assert 'test_user4' not in user['groups'][1]['admins']

