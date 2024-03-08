import datetime
from status import Status


def test_post_status():
	status = Status('user1', 'image1')
	assert status.post_status() == {'status': 'success', 'message': 'Status posted successfully.'}


def test_visibility_duration():
	status = Status('user1', 'image1', visibility_duration=0)
	assert status.is_visible() == False


def test_update_visibility_settings():
	status = Status('user1', 'image1')
	status.update_visibility_settings(0, 'nobody')
	assert status.is_visible() == False
	assert status.visible_to == 'nobody'
