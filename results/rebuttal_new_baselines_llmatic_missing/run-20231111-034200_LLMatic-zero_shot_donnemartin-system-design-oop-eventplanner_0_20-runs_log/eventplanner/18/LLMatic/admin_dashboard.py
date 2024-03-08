class AdminDashboard:
	def __init__(self):
		self.user_activities = {}
		self.system_performance_analytics = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def view_system_performance_analytics(self):
		return self.system_performance_analytics

	def manage_platform_content(self, content_id, action):
		if action == 'add':
			self.platform_content[content_id] = 'active'
		elif action == 'remove':
			self.platform_content.pop(content_id, None)
		return self.platform_content
