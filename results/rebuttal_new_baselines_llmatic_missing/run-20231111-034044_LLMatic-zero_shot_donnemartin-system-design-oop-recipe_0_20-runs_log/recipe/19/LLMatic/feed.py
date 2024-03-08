class Feed:
	def __init__(self):
		self.feed_data = {}

	def add_activity(self, user_id, activity):
		if user_id not in self.feed_data:
			self.feed_data[user_id] = []
		self.feed_data[user_id].append(activity)

	def get_recent_activity(self, user_id):
		if user_id in self.feed_data:
			return self.feed_data[user_id][-10:]
		else:
			return []
