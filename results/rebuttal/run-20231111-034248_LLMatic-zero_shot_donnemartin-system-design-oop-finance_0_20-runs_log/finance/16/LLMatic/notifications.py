class Notifications:
	def __init__(self, user):
		self.user = user
		self.notifications = []

	def add_notification(self, message):
		self.notifications.append(message)
		return self.notifications

	def alert_unusual_activity(self, transaction):
		message = f'Unusual activity detected: {transaction}'
		self.add_notification(message)

	def notify_upcoming_payment(self, bill):
		message = f'Upcoming payment due: {bill}'
		self.add_notification(message)
