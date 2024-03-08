class Feed:
	def __init__(self, user):
		self.user = user
		self.feed = []

	@classmethod
	def view(cls):
		# Here should be the logic to generate and return the feed
		pass

	def generate_feed(self):
		# Get the list of users that the current user is following
		following = self.user.get_following()

		# For each user in the following list, get their recent activity
		for user in following:
			self.feed.extend(user.get_recent_activity())

		# Sort the feed by date
		self.feed.sort(key=lambda x: x['date'], reverse=True)

		return self.feed
