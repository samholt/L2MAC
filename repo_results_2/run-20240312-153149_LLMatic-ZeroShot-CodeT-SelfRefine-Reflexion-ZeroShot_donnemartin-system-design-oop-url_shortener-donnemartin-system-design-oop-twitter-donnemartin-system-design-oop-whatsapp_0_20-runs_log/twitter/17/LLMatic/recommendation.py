class Recommendation:
	def __init__(self):
		self.users = {}
		self.interests = {}
		self.activities = {}
		self.followers = {}

	def recommend_users(self, user_id):
		recommended_users = []
		user_interests = self.interests.get(user_id, [])
		for interest in user_interests:
			for user in self.users:
				if user != user_id and interest in self.interests.get(user, []):
					recommended_users.append(user)
		return recommended_users
