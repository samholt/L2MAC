class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.booked = False

venues_db = {}


def add_venue(venue):
	venues_db[venue.id] = venue


def get_venue(id):
	return venues_db.get(id, None)


def search_venues(location, capacity, type):
	return [venue for venue in venues_db.values() if venue.location == location and venue.capacity >= capacity and venue.type == type and not venue.booked]


def book_venue(id):
	venue = get_venue(id)
	if venue and not venue.booked:
		venue.booked = True
		return True
	return False
