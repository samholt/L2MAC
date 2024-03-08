class Venue:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.booked = False

	def book_venue(self):
		if not self.booked:
			self.booked = True
			return True
		return False

	def search_venue(self, name):
		return self.name == name

	def get_location(self):
		return self.location
