class UserStatusService:
	def __init__(self):
		self.users = {}

	def set_status(self, user_id, status):
		self.users[user_id] = {'status': status}

	def get_status(self, user_id):
		if user_id not in self.users:
			return None
		return self.users[user_id]['status']
