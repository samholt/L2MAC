class Venue:
	def __init__(self, venue_id, location, capacity, venue_type):
		self.venue_id = venue_id
		self.location = location
		self.capacity = capacity
		self.venue_type = venue_type
		self.booked = False

	def book_venue(self):
		if not self.booked:
			self.booked = True
			return True
		return False

	def search_venue(self, location, capacity, venue_type):
		if self.location == location and self.capacity >= capacity and self.venue_type == venue_type:
			return True
		return False
