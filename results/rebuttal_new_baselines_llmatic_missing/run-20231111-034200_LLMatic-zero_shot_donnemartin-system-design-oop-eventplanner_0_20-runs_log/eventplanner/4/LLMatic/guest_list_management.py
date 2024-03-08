class Guest:
	def __init__(self, name, rsvp_status):
		self.name = name
		self.rsvp_status = rsvp_status


class GuestListManagement:
	def __init__(self):
		self.guest_lists = {}

	def create_guest_list(self, event_id):
		self.guest_lists[event_id] = []

	def add_guest(self, event_id, guest):
		self.guest_lists[event_id].append(guest)

	def update_guest(self, event_id, guest_name, new_rsvp_status):
		for guest in self.guest_lists[event_id]:
			if guest.name == guest_name:
				guest.rsvp_status = new_rsvp_status
				break

	def view_guest_list(self, event_id):
		return self.guest_lists[event_id]

	def import_guest_list(self, event_id, guest_list):
		self.guest_lists[event_id] = guest_list

	def export_guest_list(self, event_id):
		return self.guest_lists[event_id]
