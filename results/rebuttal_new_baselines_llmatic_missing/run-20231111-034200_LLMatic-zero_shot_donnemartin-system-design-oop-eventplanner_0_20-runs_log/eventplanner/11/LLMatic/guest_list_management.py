class GuestListManagement:
	def __init__(self):
		self.guest_lists = {}

	def create_guest_list(self, event_id):
		self.guest_lists[event_id] = []

	def add_guest(self, event_id, guest):
		self.guest_lists[event_id].append(guest)

	def remove_guest(self, event_id, guest):
		self.guest_lists[event_id].remove(guest)

	def get_guest_list(self, event_id):
		return self.guest_lists[event_id]

	def import_guest_list(self, event_id, guest_list):
		self.guest_lists[event_id] = guest_list

	def export_guest_list(self, event_id):
		return self.guest_lists[event_id]

	def track_rsvp(self, event_id, guest, rsvp):
		for g in self.guest_lists[event_id]:
			if g['name'] == guest['name']:
				g['rsvp'] = rsvp
