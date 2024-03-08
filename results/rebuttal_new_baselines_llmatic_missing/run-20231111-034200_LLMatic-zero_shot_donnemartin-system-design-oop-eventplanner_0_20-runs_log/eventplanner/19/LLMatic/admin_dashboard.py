class AdminDashboard:
	def __init__(self):
		self.user_activities = {}
		self.system_performance = {}
		self.user_engagement = {}
		self.vendor_listings = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def manage_system_performance(self, metric, value):
		self.system_performance[metric] = value

	def analyze_user_engagement(self, user_id, engagement):
		self.user_engagement[user_id] = engagement

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendor_listings[vendor_id] = listing

	def manage_platform_content(self, content_id, content):
		self.platform_content[content_id] = content
