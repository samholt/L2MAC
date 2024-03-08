import datetime
from notifications import Notification, notifications_db

def test_send_notification():
	user_id = 'user1'
	type = 'email'
	message = 'Test message'
	notification = Notification(user_id, type, message)
	notification.send_notification()
	assert notifications_db[user_id] == {'type': type, 'message': message, 'time': notification.time}

def test_set_reminder():
	user_id = 'user1'
	message = 'Test reminder'
	reminder_time = datetime.datetime.now() + datetime.timedelta(days=1)
	notification = Notification(user_id, 'reminder', message)
	notification.set_reminder(reminder_time)
	assert notifications_db[user_id] == {'type': 'reminder', 'message': message, 'time': reminder_time}
