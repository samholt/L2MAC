class Vendor:
	def __init__(self, name, profile, reviews):
		self.name = name
		self.profile = profile
		self.reviews = reviews
		self.messages = []

	def view_profile(self):
		return self.profile

	def compare_profiles(self, other_vendor):
		return self.profile == other_vendor.profile

	def view_reviews(self):
		return self.reviews

	def send_message(self, message):
		self.messages.append(message)
		return True

