import status


def test_post_status():
	status.post_status('user@test.com', 'Hello, world!', 'public')
	assert 'user@test.com' in status.status_dict


def test_set_online_status():
	status.post_status('user@test.com', 'Hello, world!', 'public')
	status.set_online_status('user@test.com', True)
	assert status.status_dict['user@test.com'].is_online
