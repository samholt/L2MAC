class Vendor:
	def __init__(self, name, services, reviews):
		self.name = name
		self.services = services
		self.reviews = reviews

	def view_vendor(self):
		return {'name': self.name, 'services': self.services, 'reviews': self.reviews}

	def compare_vendors(self, other_vendor):
		return self.services == other_vendor.services and self.reviews == other_vendor.reviews

	def send_message(self, message):
		return f'Message sent to {self.name}: {message}'

vendors_db = {}

