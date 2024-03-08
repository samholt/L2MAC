class Vendor:
	def __init__(self, name, services, reviews, messages):
		self.name = name
		self.services = services
		self.reviews = reviews
		self.messages = messages


def view_vendor_profile(vendor):
	return vendor.__dict__


def compare_vendors(vendor1, vendor2):
	return vendor1.services == vendor2.services


def communicate_with_vendor(vendor, message):
	vendor.messages.append(message)
	return vendor.messages


# Mock database
vendors = {}

