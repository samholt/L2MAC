class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_profile(self, user_id, profile):
		self.users[user_id] = profile

	def customize_profile(self, user_id, profile):
		self.users[user_id] = profile

	def get_profile(self, user_id):
		return self.users.get(user_id, None)

	def save_event(self, user_id, event):
		if 'events' not in self.users[user_id]:
			self.users[user_id]['events'] = []
		self.users[user_id]['events'].append(event)

	def get_events(self, user_id):
		return self.users[user_id].get('events', [])
