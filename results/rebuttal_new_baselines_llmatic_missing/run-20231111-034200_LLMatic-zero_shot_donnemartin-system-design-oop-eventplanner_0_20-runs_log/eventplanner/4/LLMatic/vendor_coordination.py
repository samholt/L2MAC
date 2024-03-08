class Vendor:
	def __init__(self, name, service_type, reviews):
		self.name = name
		self.service_type = service_type
		self.reviews = reviews

mock_database = {}


def view_vendor(vendor_id):
	return mock_database.get(vendor_id, 'Vendor not found')


def compare_vendors(vendor_id1, vendor_id2):
	vendor1 = mock_database.get(vendor_id1, 'Vendor not found')
	vendor2 = mock_database.get(vendor_id2, 'Vendor not found')
	return vendor1, vendor2


def send_message_to_vendor(vendor_id, message):
	vendor = mock_database.get(vendor_id, 'Vendor not found')
	if vendor != 'Vendor not found':
		return f'Message sent to {vendor.name}: {message}'
	else:
		return 'Vendor not found'
