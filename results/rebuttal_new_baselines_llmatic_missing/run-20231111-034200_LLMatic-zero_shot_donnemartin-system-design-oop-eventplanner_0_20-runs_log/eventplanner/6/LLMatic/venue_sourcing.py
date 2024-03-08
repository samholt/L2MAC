class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.booked = False

mock_database = {}


def search_venue(location, capacity, type):
	return [venue for venue in mock_database.values() if venue.location == location and venue.capacity >= capacity and venue.type == type]


def book_venue(id):
	if id in mock_database and not mock_database[id].booked:
		mock_database[id].booked = True
		return True
	return False
