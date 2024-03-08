from notifications import Notification, Reminder

def test_notification():
	notification = Notification('Email', 'Your event is coming up!')
	assert notification.type == 'Email'
	assert notification.message == 'Your event is coming up!'


def test_reminder():
	reminder = Reminder('Your event is in 1 hour', '1 hour before')
	assert reminder.message == 'Your event is in 1 hour'
	assert reminder.time == '1 hour before'
