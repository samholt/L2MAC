class WebAppService:
	def __init__(self):
		self.users = {}

	def access_web_version(self, user_id):
		self.users[user_id] = {'web_access': True}
		return True
