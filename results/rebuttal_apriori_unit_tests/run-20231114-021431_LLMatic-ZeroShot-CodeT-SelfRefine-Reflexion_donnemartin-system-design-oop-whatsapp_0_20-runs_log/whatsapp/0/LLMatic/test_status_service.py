import pytest
from status_service import StatusService


def test_post_image_status():
	status_service = StatusService()
	assert status_service.post_image_status(1, '/path/to/status_image.jpg', 24) == True


def test_set_status_visibility():
	status_service = StatusService()
	assert status_service.set_status_visibility(1, 'Everyone') == True
