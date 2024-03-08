class Vendor:
	def __init__(self, name, services, reviews):
		self.name = name
		self.services = services
		self.reviews = reviews

	def view_profile(self):
		return {'name': self.name, 'services': self.services, 'reviews': self.reviews}

	def compare_profiles(self, other_vendor):
		return {'name': self.name, 'services': self.services, 'reviews': self.reviews}, {'name': other_vendor.name, 'services': other_vendor.services, 'reviews': other_vendor.reviews}

	def send_message(self, message):
		return f'Message sent to {self.name}: {message}'

vendors = {}

