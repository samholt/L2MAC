import datetime


class Notification:
	def __init__(self, user, type):
		self.user = user
		self.type = type
		self.timestamp = datetime.datetime.now()

	def __str__(self):
		return f'{self.user} received {self.type} at {self.timestamp}'
