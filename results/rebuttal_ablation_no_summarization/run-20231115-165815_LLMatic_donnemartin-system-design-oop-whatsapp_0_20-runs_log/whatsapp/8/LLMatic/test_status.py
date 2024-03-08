import pytest
from status import Status

def test_status():
	status = Status()
	assert status.view_status() == 'No status posted yet'
	status.post_status('image.jpg', 'private')
	assert status.view_status() == {'status': 'Posted', 'image_file': 'image.jpg', 'visibility': 'private'}
	status.control_visibility('public')
	assert status.view_status() == {'status': 'Posted', 'image_file': 'image.jpg', 'visibility': 'public'}
