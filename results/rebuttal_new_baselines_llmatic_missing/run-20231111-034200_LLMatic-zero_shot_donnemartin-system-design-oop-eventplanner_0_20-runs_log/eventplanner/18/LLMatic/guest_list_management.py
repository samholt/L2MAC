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

	def import_guest_list(self, guest_list):
		for guest in guest_list:
			self.add_guest(guest['name'], guest['rsvp_status'])

	def export_guest_list(self):
		export_list = []
		for guest in self.guest_list.values():
			export_list.append({'name': guest.name, 'rsvp_status': guest.rsvp_status})
		return export_list
