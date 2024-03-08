class Admin:
	def __init__(self):
		self.user_activities = {}
		self.vendor_listings = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def manage_vendor_listings(self, vendor_id, listing):
		self.vendor_listings[vendor_id] = listing

	def manage_platform_content(self, content_id, content):
		self.platform_content[content_id] = content
