class AdminDashboard:
	def __init__(self):
		self.user_activities = {}
		self.system_performance = {}
		self.vendor_listings = {}

	def monitor_user_activities(self, user_id, activity):
		if user_id not in self.user_activities:
			self.user_activities[user_id] = []
		self.user_activities[user_id].append(activity)
		return self.user_activities

	def manage_system_performance(self, metric, value):
		self.system_performance[metric] = value
		return self.system_performance

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendor_listings[vendor_id] = listing
		return self.vendor_listings
