class Statistics:
	def __init__(self):
		self.user_engagement = {}
		self.site_usage = {}

	def monitor_user_engagement(self, user, engagement):
		self.user_engagement[user] = engagement

	def monitor_site_usage(self, usage):
		self.site_usage = usage

	def get_user_engagement(self):
		return self.user_engagement

	def get_site_usage(self):
		return self.site_usage
