class Profile:
	def __init__(self, id, user, followed_users=[]):
		self.id = id
		self.user = user
		self.followed_users = followed_users

	def create_profile(self, id, user):
		self.id = id
		self.user = user

	def add_followed_user(self, user):
		self.followed_users.append(user)

	def update_profile(self, user):
		self.user = user
