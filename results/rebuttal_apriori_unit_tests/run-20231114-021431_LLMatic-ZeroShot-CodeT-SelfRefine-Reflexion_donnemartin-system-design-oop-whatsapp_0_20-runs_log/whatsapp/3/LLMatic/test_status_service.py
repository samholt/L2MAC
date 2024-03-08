import pytest
from status_service import StatusService


def test_post_image_status():
	status_service = StatusService()
	assert status_service.post_image_status('user1', 'image1', 10) == True


def test_set_status_visibility():
	status_service = StatusService()
	status_service.post_image_status('user1', 'image1', 10)
	assert status_service.set_status_visibility('user1', 'public') == True
