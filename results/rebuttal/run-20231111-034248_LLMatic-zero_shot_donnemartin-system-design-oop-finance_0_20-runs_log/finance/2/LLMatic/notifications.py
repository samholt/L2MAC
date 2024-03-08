import datetime

class Notifications:
	def __init__(self, user):
		self.user = user
		self.notifications = []
		self.alerts = []

	def set_notification(self, notification):
		self.notifications.append(notification)

	def set_alert(self, alert):
		self.alerts.append(alert)

	def get_notifications(self):
		return self.notifications

	def get_alerts(self):
		return self.alerts

	def check_for_unusual_activity(self, transactions):
		# This is a simple example, in a real application this should be more complex
		if len(transactions) > 10:
			self.set_alert('Unusual activity detected in your account')

	def check_for_upcoming_bills(self, bills):
		# This is a simple example, in a real application this should be more complex
		for bill in bills:
			if (bill['due_date'] - datetime.datetime.now()).days <= 7:
				self.set_notification('Your bill for ' + bill['name'] + ' is due soon')

