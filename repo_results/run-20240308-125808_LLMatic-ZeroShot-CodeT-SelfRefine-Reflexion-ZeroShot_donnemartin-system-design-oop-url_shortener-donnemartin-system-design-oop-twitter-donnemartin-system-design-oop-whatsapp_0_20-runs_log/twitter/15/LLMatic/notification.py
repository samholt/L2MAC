import datetime

# Mock database
notifications_db = {}


class Notification:
	def __init__(self, user, type, post=None):
		self.user = user
		self.type = type
		self.post = post
		self.timestamp = datetime.datetime.now()

	@classmethod
	def create_notification(cls, user, type, post=None):
		notification = cls(user, type, post)
		notifications_db[notification.timestamp] = notification
		return notification
