from database import Database


class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.is_booked = False


class VenueSourcing:
	def __init__(self):
		self.db = Database()

	def add_venue(self, venue):
		self.db.insert(venue.id, venue)

	def search_venue(self, location, capacity, type):
		for venue in self.db.data.values():
			if venue.location == location and venue.capacity >= capacity and venue.type == type and not venue.is_booked:
				return venue
		return None

	def book_venue(self, id):
		venue = self.db.get(id)
		if venue != 'Data not found' and not venue.is_booked:
			venue.is_booked = True
			self.db.update(id, venue)
			return True
		return False
