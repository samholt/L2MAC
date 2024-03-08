from notification import Notification

def test_notify():
	notification = Notification('User 1')
	assert notification.notify('New recipe in your interest area') == 'Notification for User 1: New recipe in your interest area'
