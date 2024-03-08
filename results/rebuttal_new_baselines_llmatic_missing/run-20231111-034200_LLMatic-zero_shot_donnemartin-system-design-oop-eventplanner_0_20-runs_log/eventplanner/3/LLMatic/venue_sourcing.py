class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.is_booked = False

venues = {}


def find_venue(location, capacity, type):
	for venue in venues.values():
		if venue.location == location and venue.capacity >= capacity and venue.type == type and not venue.is_booked:
			return venue
	return None


def book_venue(id):
	venue = venues.get(id)
	if venue and not venue.is_booked:
		venue.is_booked = True
		return True
	return False
