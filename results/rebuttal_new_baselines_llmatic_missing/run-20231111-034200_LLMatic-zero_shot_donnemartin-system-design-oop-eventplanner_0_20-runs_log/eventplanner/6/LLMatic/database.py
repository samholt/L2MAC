class Database:
	def __init__(self):
		self.users = {}
		self.events = {}
		self.venues = {}
		self.vendors = {}
		self.budgets = {}
		self.notifications = {}
		self.reports = {}
		self.admins = {}
		self.security = {}

	def get_security_data(self, user_id):
		return self.security.get(user_id, {})

	def add_admin(self, admin_id, admin):
		self.admins[admin_id] = admin

	def add_report(self, event_id, report):
		self.reports[event_id] = report
