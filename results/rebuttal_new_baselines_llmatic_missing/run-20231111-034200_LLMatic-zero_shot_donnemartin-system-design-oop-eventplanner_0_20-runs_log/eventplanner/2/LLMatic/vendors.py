class Vendor:
	def __init__(self):
		self.vendors = {}

	def add_vendor(self, vendor_id, vendor_info):
		self.vendors[vendor_id] = vendor_info

	def get_vendor(self, vendor_id):
		return self.vendors.get(vendor_id, None)

	def get_all_vendors(self):
		return self.vendors

	def delete_vendor(self, vendor_id):
		if vendor_id in self.vendors:
			del self.vendors[vendor_id]

	def update_vendor(self, vendor_id, vendor_info):
		if vendor_id in self.vendors:
			self.vendors[vendor_id] = vendor_info
