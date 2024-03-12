import datetime


class Notification:
	def __init__(self, user_id, type):
		self.user_id = user_id
		self.type = type
		self.timestamp = datetime.datetime.now()

