class Admin:
	def __init__(self):
		self.user_activities = {}
		self.system_performance = {}
		self.vendor_listings = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def manage_system_performance(self, performance_data):
		self.system_performance = performance_data

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendor_listings[vendor_id] = listing

