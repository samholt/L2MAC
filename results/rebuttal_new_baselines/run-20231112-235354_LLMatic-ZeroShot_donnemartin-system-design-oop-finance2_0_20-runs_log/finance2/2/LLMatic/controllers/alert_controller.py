from models.alert import Alert


class AlertController:
	@staticmethod
	def create_alert(user, message):
		return Alert.create_alert(user, message)

	@staticmethod
	def get_alerts(user):
		return Alert.get_user_alerts(user)
