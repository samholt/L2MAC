from datetime import datetime

# Mock database
alerts_db = {}

class Alert:
	def __init__(self, user, alert_type, message):
		self.user = user
		self.alert_type = alert_type
		self.message = message
		self.date = datetime.now()
		if user not in alerts_db:
			alerts_db[user] = []
		alerts_db[user].append(self)

	@classmethod
	def create_alert(cls, user, alert_type, message):
		return cls(user, alert_type, message)

	@classmethod
	def get_user_alerts(cls, user):
		return alerts_db.get(user, [])

	@classmethod
	def customize_alert(cls, user, alert_type, new_message):
		for alert in alerts_db.get(user, []):
			if alert.alert_type == alert_type:
				alert.message = new_message
				return alert
		return None
