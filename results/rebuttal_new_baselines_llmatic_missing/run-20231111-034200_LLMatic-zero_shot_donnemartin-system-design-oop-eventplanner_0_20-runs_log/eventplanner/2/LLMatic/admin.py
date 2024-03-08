class Admin:
	def __init__(self):
		self.user_activities = {}
		self.system_performance = {}
		self.vendor_listings = {}

	def monitor_user_activities(self, user_id, activity):
		if user_id not in self.user_activities:
			self.user_activities[user_id] = []
		self.user_activities[user_id].append(activity)

	def get_user_activities(self, user_id):
		return self.user_activities.get(user_id, [])

	def update_system_performance(self, metric, value):
		self.system_performance[metric] = value

	def get_system_performance(self):
		return self.system_performance

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendor_listings[vendor_id] = listing

	def get_vendor_listings(self, vendor_id):
		return self.vendor_listings.get(vendor_id, None)
