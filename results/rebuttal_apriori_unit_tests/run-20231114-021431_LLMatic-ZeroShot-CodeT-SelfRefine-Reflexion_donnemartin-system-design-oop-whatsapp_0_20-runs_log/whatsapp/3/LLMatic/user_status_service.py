class UserStatusService:
	def __init__(self):
		self.users = {}

	def set_status(self, user_id, status):
		self.users[user_id] = status
		return True

	def get_status(self, user_id):
		if user_id in self.users:
			return self.users[user_id]
		return 'offline'
