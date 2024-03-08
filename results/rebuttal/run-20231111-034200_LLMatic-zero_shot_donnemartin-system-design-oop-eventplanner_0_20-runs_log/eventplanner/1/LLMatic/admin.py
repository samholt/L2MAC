class Admin:
	def __init__(self, admin_id, name):
		self.admin_id = admin_id
		self.name = name
		self.user_activities = {}
		self.system_performance_analytics = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def view_system_performance_analytics(self):
		return self.system_performance_analytics

	def manage_platform_content(self, content_id, content):
		self.platform_content[content_id] = content

	def get_platform_content(self, content_id):
		return self.platform_content.get(content_id, None)
