class Vendor:
	def __init__(self, name, service_type, reviews):
		self.name = name
		self.service_type = service_type
		self.reviews = reviews

mock_db = {}


def add_vendor(vendor):
	mock_db[vendor.name] = vendor


def remove_vendor(name):
	if name in mock_db:
		del mock_db[name]


def update_vendor(name, vendor):
	if name in mock_db:
		mock_db[name] = vendor


def get_vendor(name):
	return mock_db.get(name, None)


def compare_vendors(vendor1, vendor2):
	return vendor1.reviews > vendor2.reviews


def send_message_to_vendor(name, message):
	if name in mock_db:
		print(f'Message sent to {name}: {message}')
		return f'Message sent to {name}: {message}'
