class Vendor:
	def __init__(self, profile, reviews):
		self.profile = profile
		self.reviews = reviews

	def view_profile(self):
		return self.profile

	def compare_vendors(self, other_vendor):
		return self.reviews > other_vendor.reviews

	def communicate(self, message):
		return f"Sending message: {message} to {self.profile['name']}"
