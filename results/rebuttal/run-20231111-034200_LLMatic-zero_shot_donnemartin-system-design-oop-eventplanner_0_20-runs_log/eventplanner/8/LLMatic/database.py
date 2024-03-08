class Database:
	def __init__(self):
		self.data = {}
		self.venues = {}
		self.vendors = {}
		self.budgets = {}

	def add_event(self, event):
		self.data[event.id] = event

	def update_event(self, id, name, date, location):
		if id in self.data:
			self.data[id].update_event(name, date, location)

	def get_event(self, id):
		if id in self.data:
			return self.data[id].view_event()
		return None

	def get_all_events(self):
		return {id: event.view_event() for id, event in self.data.items()}

	def add_venue(self, venue):
		self.venues[venue.id] = venue

	def get_venue(self, id):
		if id in self.venues:
			return self.venues[id].view_venue()
		return None

	def get_all_venues(self):
		return {id: venue.view_venue() for id, venue in self.venues.items()}

	def book_venue(self, id):
		if id in self.venues:
			self.venues[id].book_venue()

	def add_vendor(self, vendor):
		self.vendors[vendor.id] = vendor

	def get_vendor(self, id):
		if id in self.vendors:
			return self.vendors[id].view_profile()
		return None

	def get_all_vendors(self):
		return {id: vendor.view_profile() for id, vendor in self.vendors.items()}

	def send_message_to_vendor(self, id, message):
		if id in self.vendors:
			self.vendors[id].send_message(message)
			return 'Message sent'
		return 'Vendor not found'

	def add_budget(self, event_id, budget):
		self.budgets[event_id] = budget

	def get_budget(self, event_id):
		if event_id in self.budgets:
			return self.budgets[event_id].get_budget_status()
		return None

	def track_expense(self, event_id, category, amount):
		if event_id in self.budgets:
			return self.budgets[event_id].track_expense(category, amount)
		return 'Event not found'
