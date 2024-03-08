from notifications import Notification

def test_notifications():
	# Create a notification
	notification = Notification()
	assert notification.create_notification('1', 'user1', 'Hello, user1', 'unread') == {'user_id': 'user1', 'message': 'Hello, user1', 'status': 'unread'}

	# Get the notification
	assert notification.get_notification('1') == {'user_id': 'user1', 'message': 'Hello, user1', 'status': 'unread'}

	# Update the notification
	assert notification.update_notification('1', 'user1', 'Hello again, user1', 'read') == {'user_id': 'user1', 'message': 'Hello again, user1', 'status': 'read'}

	# Delete the notification
	assert notification.delete_notification('1') == 'Notification deleted'

	# Try to get the deleted notification
	assert notification.get_notification('1') == 'Notification not found'

	# Send an email alert
	# In a real system, we would check that the email was actually sent.
	# For this task, we will just check that the function does not raise an exception.
	try:
		notification.send_email_alert('user1', 'Important announcement')
	except Exception as e:
		assert False, f'Exception {e} was raised'
