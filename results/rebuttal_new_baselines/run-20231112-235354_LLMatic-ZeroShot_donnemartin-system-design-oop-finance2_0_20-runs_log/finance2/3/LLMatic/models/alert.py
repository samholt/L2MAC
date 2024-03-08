class Alert:
	def __init__(self, user, alert_type, message):
		self.user = user
		self.alert_type = alert_type
		self.message = message

	@staticmethod
	def create_alert(user, alert_type, message):
		return Alert(user, alert_type, message)

	@staticmethod
	def get_user_alerts(user):
		# Mocking getting user alerts
		return [{'user': user, 'alert_type': 'Low Balance', 'message': 'Your balance is low.'}]

	def customize_alert(self, alert_type, message):
		# Mocking customizing alert
		self.alert_type = alert_type
		self.message = message
		return {'user': self.user, 'alert_type': self.alert_type, 'message': self.message}
