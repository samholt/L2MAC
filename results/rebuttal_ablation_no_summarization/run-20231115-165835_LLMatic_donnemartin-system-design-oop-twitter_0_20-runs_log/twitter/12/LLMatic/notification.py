import datetime

# Mock database
notifications_db = {}


class Notification:
	def __init__(self, username, text, trigger):
		self.username = username
		self.text = text
		self.trigger = trigger
		self.created_at = datetime.datetime.now()

	@staticmethod
	def create_notification(username, text, trigger):
		if username not in notifications_db:
			notifications_db[username] = []
		notifications_db[username].append(Notification(username, text, trigger))
		return True


# Expose the database for testing
Notification.notifications_db = notifications_db
