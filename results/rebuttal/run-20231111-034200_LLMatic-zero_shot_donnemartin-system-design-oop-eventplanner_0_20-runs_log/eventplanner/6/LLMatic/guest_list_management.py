class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, name, rsvp_status='Pending'):
		self.guest_list[name] = rsvp_status

	def update_guest(self, name, rsvp_status):
		if name in self.guest_list:
			self.guest_list[name] = rsvp_status

	def import_guests(self, guest_list):
		for guest in guest_list:
			self.add_guest(guest)

	def export_guests(self):
		return self.guest_list

	def track_rsvps(self):
		return {rsvp_status: list(names for names, status in self.guest_list.items() if status == rsvp_status) for rsvp_status in set(self.guest_list.values())}
