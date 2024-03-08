class Guest:
	def __init__(self, name, rsvp_status):
		self.name = name
		self.rsvp_status = rsvp_status


class GuestList:
	def __init__(self):
		self.guest_list = {}

	def add_guest(self, name, rsvp_status):
		self.guest_list[name] = Guest(name, rsvp_status)

	def update_guest(self, name, rsvp_status):
		if name in self.guest_list:
			self.guest_list[name].rsvp_status = rsvp_status

	def view_guest_list(self):
		return {name: guest.rsvp_status for name, guest in self.guest_list.items()}

	def import_guest_list(self, file):
		with open(file, 'r') as f:
			for line in f:
				name, rsvp_status = line.strip().split(', ')
				self.add_guest(name, rsvp_status)

	def export_guest_list(self, file):
		with open(file, 'w') as f:
			for guest in self.guest_list.values():
				f.write(f'{guest.name}, {guest.rsvp_status}\n')
