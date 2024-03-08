from notifications import Notification

def test_notification():
	user = 'test_user'
	message = 'test_message'
	notification = Notification(user, message)
	notification.send_notification()
	notification.set_reminder('2022-12-31 23:59')
	assert True
