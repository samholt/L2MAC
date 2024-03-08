import status


def test_post_status():
	status_id = status.post_status('test@test.com', 'image.jpg', ['friend@test.com'])
	assert status_id in status.statuses
	assert status.statuses[status_id]['email'] == 'test@test.com'
	assert status.statuses[status_id]['image'] == 'image.jpg'
	assert status.statuses[status_id]['visibility'] == ['friend@test.com']


def test_update_visibility():
	status_id = status.post_status('test@test.com', 'image.jpg', ['friend@test.com'])
	assert status.update_visibility('test@test.com', status_id, ['newfriend@test.com'])
	assert status.statuses[status_id]['visibility'] == ['newfriend@test.com']
	assert not status.update_visibility('wrong@test.com', status_id, ['newfriend@test.com'])
