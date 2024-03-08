class Database:
	def __init__(self):
		self.events = {}
		self.venues = {}
		self.guests = {}
		self.vendors = {}
		self.budgets = {}
		self.users = {}
		self.notifications = {}
		self.reports = {}
		self.admins = {}

	def add_event(self, event_id, event):
		self.events[event_id] = event

	def update_event(self, event_id, event):
		if event_id in self.events:
			self.events[event_id] = event

	def get_event(self, event_id):
		if event_id in self.events:
			return self.events[event_id]
		return None

	def add_venue(self, venue_id, venue):
		self.venues[venue_id] = venue

	def get_venue(self, venue_id):
		if venue_id in self.venues:
			return self.venues[venue_id]
		return None

	def add_guest(self, guest_id, guest):
		self.guests[guest_id] = guest

	def update_guest(self, guest_id, guest):
		if guest_id in self.guests:
			self.guests[guest_id] = guest

	def get_guest(self, guest_id):
		if guest_id in self.guests:
			return self.guests[guest_id]
		return None

	def add_vendor(self, vendor_id, vendor):
		self.vendors[vendor_id] = vendor

	def get_vendor(self, vendor_id):
		if vendor_id in self.vendors:
			return self.vendors[vendor_id]
		return None

	def add_budget(self, budget_id, budget):
		self.budgets[budget_id] = budget

	def get_budget(self, budget_id):
		if budget_id in self.budgets:
			return self.budgets[budget_id]
		return None

	def add_user(self, user_id, user):
		self.users[user_id] = user

	def update_user(self, user_id, user):
		if user_id in self.users:
			self.users[user_id] = user

	def get_user(self, user_id):
		if user_id in self.users:
			return self.users[user_id]
		return None

	def add_notification(self, notification_id, notification):
		self.notifications[notification_id] = notification

	def get_notification(self, notification_id):
		if notification_id in self.notifications:
			return self.notifications[notification_id]
		return None

	def add_report(self, report_id, report):
		self.reports[report_id] = report

	def get_report(self, report_id):
		if report_id in self.reports:
			return self.reports[report_id]
		return None

	def add_admin(self, admin_id, admin):
		self.admins[admin_id] = admin

	def get_admin(self, admin_id):
		if admin_id in self.admins:
			return self.admins[admin_id]
		return None
