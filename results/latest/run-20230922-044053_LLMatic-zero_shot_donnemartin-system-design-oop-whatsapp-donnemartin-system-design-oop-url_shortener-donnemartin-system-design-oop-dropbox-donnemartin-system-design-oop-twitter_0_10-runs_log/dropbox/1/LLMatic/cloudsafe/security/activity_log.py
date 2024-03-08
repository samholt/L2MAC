import datetime

# User activities will be tracked here

class ActivityLog:
	def __init__(self):
		self.log = []

	def add_activity(self, user, action):
		timestamp = datetime.datetime.now()
		self.log.append((timestamp, user, action))

	def get_activities(self, user):
		return [entry for entry in self.log if entry[1] == user]
