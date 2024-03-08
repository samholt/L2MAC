class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, event_id, guest):
		if event_id not in self.guest_list:
			self.guest_list[event_id] = []
		self.guest_list[event_id].append(guest)

	def get_guest_list(self, event_id):
		return self.guest_list.get(event_id, [])

	def import_guest_list(self, event_id, guests):
		if event_id not in self.guest_list:
			self.guest_list[event_id] = []
		self.guest_list[event_id].extend(guests)

	def export_guest_list(self, event_id):
		return self.guest_list.get(event_id, [])

	def track_rsvp(self, event_id, guest, rsvp):
		if event_id in self.guest_list:
			for g in self.guest_list[event_id]:
				if g['name'] == guest['name']:
					g['rsvp'] = rsvp
