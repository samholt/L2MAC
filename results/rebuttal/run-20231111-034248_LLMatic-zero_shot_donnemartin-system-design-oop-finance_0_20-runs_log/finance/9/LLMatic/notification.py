from datetime import datetime
from user import User


class Notification:
	def __init__(self, user: User, message: str):
		self.user = user
		self.message = message
		self.date = datetime.now()

	def alert_user(self):
		return f'Alert for {self.user.username}: {self.message} at {self.date}'


class NotificationManager:
	def __init__(self):
		self.notifications = {}

	def create_notification(self, user: User, message: str):
		notification = Notification(user, message)
		self.notifications[user.username] = notification
		return notification.alert_user()

