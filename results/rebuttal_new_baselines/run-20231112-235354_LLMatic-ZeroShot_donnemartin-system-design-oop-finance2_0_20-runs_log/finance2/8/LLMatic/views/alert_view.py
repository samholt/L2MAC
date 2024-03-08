from models.alert import Alert


class AlertView:
	@staticmethod
	def create_alert(user, alert_type, message):
		return Alert.create_alert(user, alert_type, message)

	@staticmethod
	def get_user_alerts(user):
		return Alert.get_user_alerts(user)

	@staticmethod
	def customize_alert(user, alert_type, new_message):
		return Alert.customize_alert(user, alert_type, new_message)
