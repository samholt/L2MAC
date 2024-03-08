class WebAppService:
	def __init__(self):
		self.users_online = {}

	def access_web_version(self, user_id):
		if user_id not in self.users_online:
			self.users_online[user_id] = True
		return self.users_online[user_id]
