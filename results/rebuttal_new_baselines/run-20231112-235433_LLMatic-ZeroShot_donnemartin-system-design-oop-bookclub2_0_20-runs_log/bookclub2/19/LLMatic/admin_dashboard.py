class AdminDashboard:
	def __init__(self, id, admin_user):
		self.id = id
		self.admin_user = admin_user
		self.moderation_tools = []

	def create_dashboard(self, id, admin_user):
		self.id = id
		self.admin_user = admin_user

	def add_moderation_tool(self, tool):
		self.moderation_tools.append(tool)

	def update_dashboard(self, id=None, admin_user=None):
		if id is not None:
			self.id = id
		if admin_user is not None:
			self.admin_user = admin_user
