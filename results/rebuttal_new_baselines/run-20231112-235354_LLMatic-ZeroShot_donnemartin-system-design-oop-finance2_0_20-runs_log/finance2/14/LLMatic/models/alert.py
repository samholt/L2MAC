class Alert:
	def __init__(self, user, message, alert_type):
		self.user = user
		self.message = message
		self.alert_type = alert_type

	@classmethod
	def create_alert(cls, user, message, alert_type):
		return cls(user, message, alert_type)

	@staticmethod
	def get_user_alerts(user):
		# Mock database
		alerts_db = {
			'user1': [
				Alert('user1', 'Low balance', 'warning'),
				Alert('user1', 'Transaction alert', 'info')
			],
			'user2': [
				Alert('user2', 'Investment alert', 'info')
			]
		}
		return alerts_db.get(user, [])

	def customize_alert(self, new_message, new_alert_type):
		self.message = new_message
		self.alert_type = new_alert_type
