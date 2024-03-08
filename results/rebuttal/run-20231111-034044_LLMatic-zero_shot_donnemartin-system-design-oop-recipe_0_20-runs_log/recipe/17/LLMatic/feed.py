class Feed:
	def __init__(self):
		self.activities = {}

	def add_activity(self, user_id, activity):
		if user_id not in self.activities:
			self.activities[user_id] = []
		self.activities[user_id].append(activity)

	def get_feed(self, user_id, follow):
		feed = []
		followees = follow.get_followees(user_id)
		for followee in followees:
			if followee in self.activities:
				feed.extend(self.activities[followee])
		return sorted(feed, reverse=True)
