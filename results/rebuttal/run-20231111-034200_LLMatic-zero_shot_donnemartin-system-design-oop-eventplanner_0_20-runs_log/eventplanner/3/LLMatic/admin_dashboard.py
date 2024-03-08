class Admin:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.user_activities = {}
		self.system_performance = {}
		self.platform_content = {}

	def monitor_user_activities(self, user_id, activity):
		self.user_activities[user_id] = activity

	def monitor_system_performance(self, performance_data):
		self.system_performance = performance_data

	def manage_platform_content(self, content):
		self.platform_content = content


def view_dashboard(admin):
	return {'user_activities': admin.user_activities, 'system_performance': admin.system_performance, 'platform_content': admin.platform_content}
