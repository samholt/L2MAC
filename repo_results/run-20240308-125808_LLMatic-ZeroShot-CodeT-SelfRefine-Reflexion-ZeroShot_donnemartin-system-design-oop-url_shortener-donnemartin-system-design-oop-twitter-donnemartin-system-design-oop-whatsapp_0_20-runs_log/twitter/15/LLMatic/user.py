class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.following = []
		self.followers = []
		self.blocked_users = []

	def follow_user(self, user):
		self.following.append(user)
		user.followers.append(self)

	def unfollow_user(self, user):
		self.following.remove(user)
		user.followers.remove(self)

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def block_user(self, user):
		self.blocked_users.append(user)
		return 'User blocked.'

	def get_user_recommendations(self):
		recommendations = []
		for user in self.following:
			for potential in user.following:
				if potential not in self.following and potential not in self.blocked_users and potential not in recommendations:
					recommendations.append(potential)
		return recommendations
