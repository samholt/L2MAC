class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, name, email):
		self.guest_list[email] = {'name': name, 'RSVP': False}

	def remove_guest(self, email):
		if email in self.guest_list:
			del self.guest_list[email]

	def import_guest_list(self, guest_list):
		self.guest_list = guest_list

	def export_guest_list(self):
		return self.guest_list

	def update_rsvp(self, email, rsvp):
		if email in self.guest_list:
			self.guest_list[email]['RSVP'] = rsvp
