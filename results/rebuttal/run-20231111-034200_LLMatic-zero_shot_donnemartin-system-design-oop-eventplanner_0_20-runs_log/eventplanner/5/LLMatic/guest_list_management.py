class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, guest_id, guest_info):
		self.guest_list[guest_id] = guest_info

	def update_guest(self, guest_id, guest_info):
		if guest_id in self.guest_list:
			self.guest_list[guest_id] = guest_info

	def import_guests(self, guest_list):
		self.guest_list = guest_list

	def export_guests(self):
		return self.guest_list

	def track_rsvp(self, guest_id, rsvp_status):
		if guest_id in self.guest_list:
			self.guest_list[guest_id]['rsvp'] = rsvp_status
