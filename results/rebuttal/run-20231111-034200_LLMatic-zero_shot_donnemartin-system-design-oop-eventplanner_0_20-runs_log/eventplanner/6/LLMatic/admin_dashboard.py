class Admin:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.users = {}
		self.analytics = {}
		self.vendors = {}

	def monitor_user_activities(self, user_id, activity):
		self.users[user_id] = activity
		return self.users[user_id]

	def view_system_performance(self, analytics):
		self.analytics = analytics
		return self.analytics

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendors[vendor_id] = listing
		return self.vendors[vendor_id]
