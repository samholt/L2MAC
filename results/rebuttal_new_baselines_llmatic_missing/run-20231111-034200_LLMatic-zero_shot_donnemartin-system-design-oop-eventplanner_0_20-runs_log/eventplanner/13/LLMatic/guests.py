class Guest:
	def __init__(self):
		self.guest_list = {}

	def create_guest(self, guest_id, name, email, phone):
		self.guest_list[guest_id] = {'name': name, 'email': email, 'phone': phone, 'rsvp': False}

	def update_guest(self, guest_id, name=None, email=None, phone=None):
		if guest_id in self.guest_list:
			if name:
				self.guest_list[guest_id]['name'] = name
			if email:
				self.guest_list[guest_id]['email'] = email
			if phone:
				self.guest_list[guest_id]['phone'] = phone

	def view_guests(self):
		return self.guest_list

	def import_guests(self, guests):
		self.guest_list.update(guests)

	def export_guests(self):
		return self.guest_list

	def track_rsvp(self, guest_id, rsvp):
		if guest_id in self.guest_list:
			self.guest_list[guest_id]['rsvp'] = rsvp
