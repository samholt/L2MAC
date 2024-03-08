from datetime import datetime


class ActivityLog:
	def __init__(self, user, action):
		self.user = user
		self.action = action
		self.date_time = datetime.now()

	def __str__(self):
		return f'User: {self.user}, Action: {self.action}, Date/Time: {self.date_time}'
