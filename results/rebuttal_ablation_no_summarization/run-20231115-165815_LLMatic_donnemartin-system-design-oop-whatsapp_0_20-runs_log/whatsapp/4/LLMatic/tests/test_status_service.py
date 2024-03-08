import pytest
from services.status_service import StatusService


def test_post_status():
	service = StatusService()
	status = service.post_status('1', 'user1', 'image1', 'public', '1h')
	assert status.id == '1'
	assert status.user == 'user1'
	assert status.image == 'image1'
	assert status.visibility == 'public'
	assert status.time_limit == '1h'


def test_set_visibility():
	service = StatusService()
	service.post_status('1', 'user1', 'image1', 'public', '1h')
	service.set_visibility('1', 'private')
	status = service.status_db.get('1')
	assert status.visibility == 'private'


def test_set_time_limit():
	service = StatusService()
	service.post_status('1', 'user1', 'image1', 'public', '1h')
	service.set_time_limit('1', '2h')
	status = service.status_db.get('1')
	assert status.time_limit == '2h'
