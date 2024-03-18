import notification


def test_create_notification():
	n = notification.Notification()
	n.create_notification('user1', 'content1')
	assert len(n.get_notifications('user1')) == 1


def test_get_notifications():
	n = notification.Notification()
	n.create_notification('user1', 'content1')
	n.create_notification('user1', 'content2')
	assert len(n.get_notifications('user1')) == 2
