class Alert:
	alerts = []

	def __init__(self, user, alert_type, message):
		self.user = user
		self.alert_type = alert_type
		self.message = message
		self.alerts.append(self)

	@classmethod
	def create_alert(cls, user, alert_type, message):
		alert = cls(user, alert_type, message)
		return alert

	@classmethod
	def get_user_alerts(cls, user):
		# This is a mock database operation
		# In a real application, this would involve a database query
		alerts = [alert for alert in cls.alerts if alert.user == user]
		return alerts
