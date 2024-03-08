class Feed:
	def __init__(self):
		self.activities = {}

	def add_activity(self, user, activity):
		if user not in self.activities:
			self.activities[user] = []
		self.activities[user].append(activity)

	def get_feed(self, user):
		return self.activities.get(user, [])
