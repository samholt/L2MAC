class Notification:
	def __init__(self, username):
		self.username = username
		self.notifications = []

	def send_notification(self, message):
		print(f'Sending notification to {self.username}: {message}')
		self.notifications.append(message)

	def set_bill_notification(self, bill):
		message = f'Upcoming bill: {bill}'
		self.send_notification(message)

	def set_payment_notification(self, payment):
		message = f'Upcoming payment: {payment}'
		self.send_notification(message)

	def alert_unusual_activity(self, activity):
		message = f'Alert! Unusual activity detected: {activity}'
		self.send_notification(message)

	def get_notifications(self):
		return self.notifications
