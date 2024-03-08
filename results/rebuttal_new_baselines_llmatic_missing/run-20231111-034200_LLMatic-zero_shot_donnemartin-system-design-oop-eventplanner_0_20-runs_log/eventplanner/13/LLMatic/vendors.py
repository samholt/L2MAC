class Vendor:
	def __init__(self):
		self.vendors = {}

	def add_vendor(self, vendor_id, vendor_details):
		self.vendors[vendor_id] = vendor_details

	def view_vendor(self, vendor_id):
		return self.vendors.get(vendor_id, {})

	def compare_vendors(self, vendor_id1, vendor_id2):
		vendor1 = self.vendors.get(vendor_id1, {})
		vendor2 = self.vendors.get(vendor_id2, {})
		return vendor1, vendor2

	def message_vendor(self, vendor_id, message):
		vendor = self.vendors.get(vendor_id, {})
		if vendor:
			vendor['messages'].append(message)
			return True
		return False
