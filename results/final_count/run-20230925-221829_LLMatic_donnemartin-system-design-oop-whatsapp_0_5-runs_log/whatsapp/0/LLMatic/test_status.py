import pytest
from status import Status

def test_post_status():
	status = Status()
	status.post_status('user1', 'Hello World!', 'public')
	assert status.status_db['user1'][0]['status'] == 'Hello World!'
	assert status.status_db['user1'][0]['visibility'] == 'public'

def test_view_statuses():
	status = Status()
	status.post_status('user1', 'Hello World!', 'public')
	status.post_status('user2', 'Hello again!', 'private')
	visible_statuses = status.view_statuses('user1')
	assert len(visible_statuses) == 1
	assert visible_statuses[0]['status'] == 'Hello World!'

def test_manage_status_visibility():
	status = Status()
	status.post_status('user1', 'Hello World!', 'public')
	status_id = id(status.status_db['user1'][0])
	assert status.manage_status_visibility('user1', status_id, 'private')
	assert status.status_db['user1'][0]['visibility'] == 'private'
