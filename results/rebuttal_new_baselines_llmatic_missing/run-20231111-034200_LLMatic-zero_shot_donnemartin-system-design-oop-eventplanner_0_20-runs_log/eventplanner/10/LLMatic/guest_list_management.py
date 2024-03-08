class Guest:
	def __init__(self, name, rsvp_status):
		self.name = name
		self.rsvp_status = rsvp_status


class GuestListManagement:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, guest):
		self.guest_list[guest.name] = guest.rsvp_status

	def update_guest(self, name, rsvp_status):
		if name in self.guest_list:
			self.guest_list[name] = rsvp_status

	def view_guest_list(self):
		return self.guest_list

	def import_guest_list(self, guest_list):
		self.guest_list = guest_list

	def export_guest_list(self):
		return self.guest_list
