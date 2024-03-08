class VendorCoordination:
	def __init__(self):
		self.vendors = {}

	def add_vendor(self, vendor_id, vendor_info):
		self.vendors[vendor_id] = vendor_info

	def get_vendor(self, vendor_id):
		return self.vendors.get(vendor_id, None)

	def compare_vendors(self, vendor_id1, vendor_id2):
		vendor1 = self.get_vendor(vendor_id1)
		vendor2 = self.get_vendor(vendor_id2)
		if not vendor1 or not vendor2:
			return None
		return vendor1['rating'] - vendor2['rating']

	def send_message(self, vendor_id, message):
		vendor = self.get_vendor(vendor_id)
		if not vendor:
			return None
		vendor['messages'].append(message)
		return True
