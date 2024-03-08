class Notification:
	def __init__(self):
		self.notifications = {}

	def create_notification(self, notification_id, user_id, message, status):
		self.notifications[notification_id] = {'user_id': user_id, 'message': message, 'status': status}
		return self.notifications[notification_id]

	def get_notification(self, notification_id):
		return self.notifications.get(notification_id, 'Notification not found')

	def update_notification(self, notification_id, user_id, message, status):
		if notification_id in self.notifications:
			self.notifications[notification_id] = {'user_id': user_id, 'message': message, 'status': status}
			return self.notifications[notification_id]
		return 'Notification not found'

	def delete_notification(self, notification_id):
		if notification_id in self.notifications:
			del self.notifications[notification_id]
			return 'Notification deleted'
		return 'Notification not found'

	def send_email_alert(self, user_id, message):
		# In a real system, here we would use an email service to send the email.
		# For this task, we will just print the message to the console.
		print(f'Sending email to user {user_id} with message: {message}')
