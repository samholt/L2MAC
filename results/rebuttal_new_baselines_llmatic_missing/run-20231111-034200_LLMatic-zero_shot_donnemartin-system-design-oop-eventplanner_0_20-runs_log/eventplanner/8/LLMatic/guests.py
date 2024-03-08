class Guest:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.rsvp_status = False

	def rsvp(self):
		self.rsvp_status = True


class GuestList:
	def __init__(self):
		self.guests = {}

	def add_guest(self, name, email):
		guest = Guest(name, email)
		self.guests[email] = guest

	def remove_guest(self, email):
		if email in self.guests:
			del self.guests[email]

	def get_guest(self, email):
		return self.guests.get(email, None)

	def import_guests(self, guest_list):
		for guest in guest_list:
			self.add_guest(guest['name'], guest['email'])

	def export_guests(self):
		return [{'name': guest.name, 'email': guest.email} for guest in self.guests.values()]

	def track_rsvps(self):
		return {email: guest.rsvp_status for email, guest in self.guests.items()}
