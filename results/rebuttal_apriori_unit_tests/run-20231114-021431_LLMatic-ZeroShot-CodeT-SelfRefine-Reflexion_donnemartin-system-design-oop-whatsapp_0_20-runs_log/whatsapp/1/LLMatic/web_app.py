class WebAppService:
	def __init__(self):
		self.user_web_links = {}

	def access_web_version(self, user_id):
		if user_id not in self.user_web_links:
			self.user_web_links[user_id] = f'https://chatapp.com/user/{user_id}'
		return self.user_web_links[user_id]
