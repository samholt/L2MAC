class Venue:
	def __init__(self, name, location, capacity, type):
		self.name = name
		self.location = location
		self.capacity = capacity
		self.type = type
		self.is_booked = False

	def book_venue(self):
		if not self.is_booked:
			self.is_booked = True
			return True
		return False

	def get_venue_details(self):
		return {'name': self.name, 'location': self.location, 'capacity': self.capacity, 'type': self.type, 'is_booked': self.is_booked}


class VenueSourcing:
	def __init__(self):
		self.venues = []

	def add_venue(self, name, location, capacity, type):
		venue = Venue(name, location, capacity, type)
		self.venues.append(venue)

	def search_venues(self, capacity, type):
		available_venues = [venue for venue in self.venues if venue.capacity >= capacity and venue.type == type and not venue.is_booked]
		return available_venues

	def book_venue(self, name):
		for venue in self.venues:
			if venue.name == name:
				return venue.book_venue()
		return False
