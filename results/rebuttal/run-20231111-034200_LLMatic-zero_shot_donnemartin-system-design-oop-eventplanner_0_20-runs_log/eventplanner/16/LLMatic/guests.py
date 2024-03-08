class Guest:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, name, rsvp_status):
		self.guest_list[name] = rsvp_status

	def update_guest(self, name, rsvp_status):
		if name in self.guest_list:
			self.guest_list[name] = rsvp_status

	def view_guests(self):
		return self.guest_list

	def import_guests(self, guest_list):
		self.guest_list = guest_list

	def export_guests(self):
		return self.guest_list
