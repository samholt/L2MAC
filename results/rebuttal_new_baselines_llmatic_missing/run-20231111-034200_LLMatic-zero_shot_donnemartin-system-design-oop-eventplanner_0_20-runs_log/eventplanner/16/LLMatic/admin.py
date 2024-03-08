class Admin:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.user_activities = {}
		self.system_performance = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def manage_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def view_system_performance(self):
		return self.system_performance

	def manage_vendor_listings(self, vendor_id, listing):
		self.platform_content[vendor_id] = listing

	def manage_platform_content(self, content_id, content):
		self.platform_content[content_id] = content

admins = {}

