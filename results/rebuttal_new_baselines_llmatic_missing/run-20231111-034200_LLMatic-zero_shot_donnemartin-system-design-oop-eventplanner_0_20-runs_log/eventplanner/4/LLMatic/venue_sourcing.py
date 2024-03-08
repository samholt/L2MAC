class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.is_booked = False


class VenueSourcing:
	def __init__(self):
		self.venues = {}

	def add_venue(self, id, location, capacity, type):
		self.venues[id] = Venue(id, location, capacity, type)

	def search_venue(self, capacity, type):
		for id, venue in self.venues.items():
			if venue.capacity >= capacity and venue.type == type and not venue.is_booked:
				return venue
		return None

	def book_venue(self, id):
		if id in self.venues and not self.venues[id].is_booked:
			self.venues[id].is_booked = True
			return True
		return False
