import status

def test_post_status():
	s = status.Status()
	assert s.post_status('user1', 'image.jpg', 'public') == 'Status posted successfully'
	assert len(s.status_db) == 1
	assert s.status_db[1] == {'user_id': 'user1', 'image_file': 'image.jpg', 'visibility': 'public'}


def test_control_visibility():
	s = status.Status()
	s.post_status('user1', 'image.jpg', 'public')
	assert s.control_visibility('user1', 1, 'private') == 'Visibility updated successfully'
	assert s.status_db[1]['visibility'] == 'private'
	assert s.control_visibility('user2', 1, 'public') == 'Status not found or user not authorized'


def test_queue_message():
	s = status.Status()
	s.user_status['user1'] = 'offline'
	assert s.queue_message('user2', 'user1', 'Hello') == 'Message queued'
	assert len(s.message_queue['user1']) == 1
	assert s.message_queue['user1'][0] == {'sender_id': 'user2', 'message': 'Hello'}


def test_display_status():
	s = status.Status()
	assert s.display_status('user1') == 'offline'
	s.user_status['user1'] = 'online'
	assert s.display_status('user1') == 'online'
