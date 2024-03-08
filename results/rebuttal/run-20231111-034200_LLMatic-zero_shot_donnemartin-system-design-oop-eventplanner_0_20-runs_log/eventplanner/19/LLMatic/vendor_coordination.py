class VendorCoordination:
	def __init__(self):
		self.vendors = {}
		self.messages = {}

	def add_vendor(self, vendor_id, vendor_details):
		self.vendors[vendor_id] = vendor_details

	def view_vendor(self, vendor_id):
		return self.vendors.get(vendor_id, 'Vendor not found')

	def compare_vendors(self, vendor_id1, vendor_id2):
		return self.vendors.get(vendor_id1, 'Vendor not found'), self.vendors.get(vendor_id2, 'Vendor not found')

	def send_message(self, vendor_id, message):
		if vendor_id not in self.messages:
			self.messages[vendor_id] = []
		self.messages[vendor_id].append(message)

	def view_messages(self, vendor_id):
		return self.messages.get(vendor_id, 'No messages found')
