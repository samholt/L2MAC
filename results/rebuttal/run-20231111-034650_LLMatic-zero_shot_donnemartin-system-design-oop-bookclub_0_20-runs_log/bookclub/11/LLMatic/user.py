class User:
	def __init__(self, name, interests):
		self.name = name
		self.interests = interests
		self.book_lists = {}
		self.following = []
		self.followers = []

	def follow_user(self, user_to_follow):
		self.following.append(user_to_follow)
		user_to_follow.followers.append(self)

users = {}
