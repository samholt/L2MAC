class Guest:
	def __init__(self, name, contact_info, rsvp_status):
		self.name = name
		self.contact_info = contact_info
		self.rsvp_status = rsvp_status

	def update_rsvp_status(self, rsvp_status):
		self.rsvp_status = rsvp_status

	def get_guest_info(self):
		return {'name': self.name, 'contact_info': self.contact_info, 'rsvp_status': self.rsvp_status}
