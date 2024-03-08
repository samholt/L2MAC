class Vendor:
	def __init__(self, name, service_type, profile, reviews):
		self.name = name
		self.service_type = service_type
		self.profile = profile
		self.reviews = reviews

	def view_vendor(self):
		return {'name': self.name, 'service_type': self.service_type, 'profile': self.profile, 'reviews': self.reviews}

	def compare_to(self, other_vendor):
		return self.service_type == other_vendor.service_type

	def send_message(self, message):
		return f'Message sent to {self.name}: {message}'
