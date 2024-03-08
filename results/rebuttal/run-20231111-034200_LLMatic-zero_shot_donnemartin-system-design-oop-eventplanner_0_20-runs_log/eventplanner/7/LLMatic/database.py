class Database:
	def __init__(self):
		self.venues = {}
		self.admins = {}
		self.security_details = {}

	def add_venue(self, venue_id, venue_details):
		self.venues[venue_id] = venue_details

	def get_venue(self, venue_id):
		return self.venues.get(venue_id, None)

	def search_venues(self, search_term):
		return {k: v for k, v in self.venues.items() if search_term in v['name']}

	def add_admin(self, admin_id, admin_details):
		self.admins[admin_id] = admin_details

	def get_admin(self, admin_id):
		return self.admins.get(admin_id, None)

	def add_security_detail(self, user_id, security_detail):
		self.security_details[user_id] = security_detail

	def get_security_detail(self, user_id):
		return self.security_details.get(user_id, None)
