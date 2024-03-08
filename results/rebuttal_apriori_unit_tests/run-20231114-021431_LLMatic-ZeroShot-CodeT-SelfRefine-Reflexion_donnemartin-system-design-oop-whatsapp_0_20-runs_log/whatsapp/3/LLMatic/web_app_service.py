class WebAppService:
	def __init__(self):
		self.users = {}

	def access_web_version(self, user_id):
		if user_id in self.users:
			return True
		return False
