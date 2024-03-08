class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, event_id, guest_name):
		if event_id not in self.guest_list:
			self.guest_list[event_id] = []
		self.guest_list[event_id].append(guest_name)

	def remove_guest(self, event_id, guest_name):
		if event_id in self.guest_list and guest_name in self.guest_list[event_id]:
			self.guest_list[event_id].remove(guest_name)

	def get_guest_list(self, event_id):
		return self.guest_list.get(event_id, [])

	def import_guest_list(self, event_id, guest_list):
		self.guest_list[event_id] = guest_list

	def export_guest_list(self, event_id):
		return self.guest_list.get(event_id, [])

	def track_rsvp(self, event_id, guest_name, rsvp_status):
		if event_id in self.guest_list and guest_name in self.guest_list[event_id]:
			index = self.guest_list[event_id].index(guest_name)
			self.guest_list[event_id][index] = (guest_name, rsvp_status)
