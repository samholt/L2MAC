class Guest:
	def __init__(self, name, rsvp_status):
		self.name = name
		self.rsvp_status = rsvp_status


class GuestList:
	def __init__(self):
		self.guests = {}

	def add_guest(self, name, rsvp_status):
		self.guests[name] = Guest(name, rsvp_status)

	def get_guest(self, name):
		return self.guests.get(name, None)

	def import_guests(self, guest_list):
		for guest in guest_list:
			self.add_guest(guest['name'], guest['rsvp_status'])

	def export_guests(self):
		return [{'name': guest.name, 'rsvp_status': guest.rsvp_status} for guest in self.guests.values()]

	def manage_guest(self, name, rsvp_status):
		guest = self.get_guest(name)
		if guest:
			guest.rsvp_status = rsvp_status
