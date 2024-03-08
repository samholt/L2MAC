class Venue:
	def __init__(self, id, name, location, capacity, type):
		self.id = id
		self.name = name
		self.location = location
		self.capacity = capacity
		self.type = type


class VenueSourcing:
	def __init__(self):
		self.venues = {}

	def add_venue(self, id, name, location, capacity, type):
		self.venues[id] = Venue(id, name, location, capacity, type)

	def search_venues(self, location=None, capacity=None, type=None):
		results = []
		for id, venue in self.venues.items():
			if location and venue.location != location:
				continue
			if capacity and venue.capacity < capacity:
				continue
			if type and venue.type != type:
				continue
			results.append(venue)
		return results

	def book_venue(self, id):
		if id in self.venues:
			return True
		return False
