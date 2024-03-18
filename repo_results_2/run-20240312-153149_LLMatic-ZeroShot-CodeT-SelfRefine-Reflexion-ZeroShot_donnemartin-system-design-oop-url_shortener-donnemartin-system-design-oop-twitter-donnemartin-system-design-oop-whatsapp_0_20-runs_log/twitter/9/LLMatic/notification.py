import datetime


class Notification:
	def __init__(self):
		self.db = {}

	def create_notification(self, user, content):
		timestamp = datetime.datetime.now()
		if user not in self.db:
			self.db[user] = []
		self.db[user].append({'content': content, 'timestamp': timestamp})

	def get_notifications(self, user):
		return self.db.get(user, [])
