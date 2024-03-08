class Vendor:
	def __init__(self, name, service_type, reviews):
		self.name = name
		self.service_type = service_type
		self.reviews = reviews

	def view_profile(self):
		return {'name': self.name, 'service_type': self.service_type, 'reviews': self.reviews}

	def compare_to(self, other_vendor):
		return self.service_type == other_vendor.service_type

	def send_message(self, message):
		return f'Message sent to {self.name}: {message}'


# Mock database
vendors_db = {}


def add_vendor_to_db(vendor):
	vendors_db[vendor.name] = vendor


def get_vendor_from_db(name):
	return vendors_db.get(name, None)


def get_all_vendors_from_db():
	return list(vendors_db.values())
