class GuestListManagement:
	def __init__(self):
		self.guest_lists = {}

	def create_guest_list(self, event_id, guest_list):
		self.guest_lists[event_id] = guest_list

	def get_guest_list(self, event_id):
		return self.guest_lists.get(event_id, [])

	def update_guest_list(self, event_id, guest_list):
		self.guest_lists[event_id] = guest_list

	def delete_guest_list(self, event_id):
		if event_id in self.guest_lists:
			del self.guest_lists[event_id]

	def import_guest_list(self, event_id, guest_list):
		self.guest_lists[event_id] = guest_list

	def export_guest_list(self, event_id):
		return self.guest_lists.get(event_id, [])

	def track_rsvp(self, event_id, guest_name, rsvp_status):
		if event_id in self.guest_lists:
			for guest in self.guest_lists[event_id]:
				if guest['name'] == guest_name:
					guest['rsvp'] = rsvp_status
