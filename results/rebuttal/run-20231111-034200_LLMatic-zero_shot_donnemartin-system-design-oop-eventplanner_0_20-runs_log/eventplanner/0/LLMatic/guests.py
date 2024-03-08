class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, guest_id, guest_info):
		self.guest_list[guest_id] = guest_info

	def get_guest(self, guest_id):
		return self.guest_list.get(guest_id, None)

	def remove_guest(self, guest_id):
		if guest_id in self.guest_list:
			del self.guest_list[guest_id]

	def import_guest_list(self, guest_list):
		self.guest_list.update(guest_list)

	def export_guest_list(self):
		return self.guest_list

	def track_rsvp(self, guest_id, rsvp_status):
		if guest_id in self.guest_list:
			self.guest_list[guest_id]['rsvp'] = rsvp_status
