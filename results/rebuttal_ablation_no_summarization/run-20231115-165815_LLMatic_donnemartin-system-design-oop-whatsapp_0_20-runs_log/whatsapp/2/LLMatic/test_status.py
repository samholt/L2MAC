import time
from status import Status


def test_post_status():
	status = Status()
	status_id = status.post_status('user1', 'image1', 'public')
	assert status_id == 1
	assert status.statuses[status_id]['user_id'] == 'user1'
	assert status.statuses[status_id]['image'] == 'image1'
	assert status.statuses[status_id]['visibility'] == 'public'


def test_control_status_visibility():
	status = Status()
	status_id = status.post_status('user1', 'image1', 'public')
	assert status.control_status_visibility(status_id, 'private')
	assert status.statuses[status_id]['visibility'] == 'private'


def test_status_expiration():
	status = Status()
	status_id = status.post_status('user1', 'image1', 'public')
	time.sleep(2)
	assert time.time() - status.statuses[status_id]['time_posted'] < 86400


def test_set_online_status():
	status = Status()
	status.set_online_status('user1', 'online')
	assert status.online_status['user1'] == 'online'
	status.set_online_status('user1', 'offline')
	assert status.online_status['user1'] == 'offline'


def test_queue_message():
	status = Status()
	status.queue_message('user1', 'user2', 'Hello!')
	assert ('user1', 'Hello!') in status.message_queue['user2']


def test_display_status():
	status = Status()
	status.post_status('user1', 'image1', 'public')
	status.set_online_status('user1', 'online')
	assert status.display_status('user1') == ('public', 'online')
