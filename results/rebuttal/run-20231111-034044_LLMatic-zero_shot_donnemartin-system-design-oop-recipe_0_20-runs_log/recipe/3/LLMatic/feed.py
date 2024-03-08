class Feed:
	def __init__(self, user):
		self.user = user
		self.feed = []

	def show_recent_activity(self):
		# Get the list of users that the current user is following
		following = self.user.get_following()
		
		# For each user in the following list, get their recent activity
		for user in following:
			self.feed.extend(user.get_recent_activity())
		
		# Sort the feed by timestamp in descending order
		self.feed.sort(key=lambda x: x['timestamp'], reverse=True)
		
		return self.feed
