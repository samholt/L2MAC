from datetime import datetime

class Alert:
	alerts = []

	def __init__(self, user, alert_type, message):
		self.user = user
		self.alert_type = alert_type
		self.message = message
		self.date = datetime.now()
		Alert.alerts.append(self)

	@classmethod
	def create_alert(cls, user, message):
		return cls(user, 'alert', message)

	@staticmethod
	def get_user_alerts(user):
		return [alert for alert in Alert.alerts if alert.user == user]

	def to_dict(self):
		return {
			'user': self.user,
			'alert_type': self.alert_type,
			'message': self.message,
			'date': self.date
		}
