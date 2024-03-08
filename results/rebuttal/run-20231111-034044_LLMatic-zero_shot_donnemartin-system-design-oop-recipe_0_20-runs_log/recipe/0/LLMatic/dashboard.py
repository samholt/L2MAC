class Dashboard:
	def __init__(self, admin):
		self.admin = admin
		self.user_engagement = {}
		self.site_usage = {}

	def monitor_user_engagement(self, user):
		self.user_engagement[user.username] = len(user.submitted_recipes)
		return self.user_engagement

	def monitor_site_usage(self, users):
		self.site_usage['Site'] = len(users)
		return self.site_usage
