class User:
	def __init__(self):
		self.users = {}

	def create_user(self, user_id, name, email):
		self.users[user_id] = {'name': name, 'email': email, 'events': []}

	def update_user(self, user_id, name=None, email=None):
		if user_id in self.users:
			if name:
				self.users[user_id]['name'] = name
			if email:
				self.users[user_id]['email'] = email

	def save_event(self, user_id, event_id):
		if user_id in self.users:
			self.users[user_id]['events'].append(event_id)

	def get_user(self, user_id):
		return self.users.get(user_id, None)
