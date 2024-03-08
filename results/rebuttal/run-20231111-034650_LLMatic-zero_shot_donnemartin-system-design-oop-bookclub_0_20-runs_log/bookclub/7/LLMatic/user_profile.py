class UserProfile:
	def __init__(self):
		self.profiles = {}

	def create_profile(self, user_id, name):
		self.profiles[user_id] = {'name': name, 'books': [], 'following': []}

	def list_books(self, user_id):
		return self.profiles[user_id]['books']

	def follow(self, user_id, user_id_to_follow):
		self.profiles[user_id]['following'].append(user_id_to_follow)
