import notifications

def test_notifications():
	n = notifications.Notification()
	n.add_notification('user1', 'Test message 1')
	n.add_notification('user1', 'Test message 2')
	assert len(n.get_notifications('user1')) == 2
	assert n.get_notifications('user1')[0] == 'Test message 1'
	assert n.get_notifications('user1')[1] == 'Test message 2'
	n.clear_notifications('user1')
	assert len(n.get_notifications('user1')) == 0
