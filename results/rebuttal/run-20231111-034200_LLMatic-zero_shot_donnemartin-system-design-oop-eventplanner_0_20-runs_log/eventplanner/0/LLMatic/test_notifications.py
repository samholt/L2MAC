import pytest
from notifications import Notifications

def test_notifications():
	notifications = Notifications()

	user_id = 'user1'
	message = 'Test message'

	notifications.add_notification(user_id, message)
	assert notifications.get_notifications(user_id) == [message]

	notifications.clear_notifications(user_id)
	assert notifications.get_notifications(user_id) == []

	def test_reminders():
		notifications = Notifications()

		user_id = 'user1'
		event_id = 'event1'
		reminder_time = '2022-12-31 23:59:59'

		notifications.set_reminder(user_id, event_id, reminder_time)
		assert notifications.get_reminders(user_id) == [{'event_id': event_id, 'reminder_time': reminder_time}]
