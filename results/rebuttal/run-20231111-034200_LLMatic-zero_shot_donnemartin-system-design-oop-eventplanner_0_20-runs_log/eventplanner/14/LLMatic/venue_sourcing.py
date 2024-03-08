class Venue:
	def __init__(self, id, name, location, capacity, type):
		self.id = id
		self.name = name
		self.location = location
		self.capacity = capacity
		self.type = type
		self.booked = False

	def book_venue(self):
		if not self.booked:
			self.booked = True
			return True
		return False

	def get_location(self):
		return self.location


venues = [
	Venue('1', 'Venue 1', 'Location 1', 100, 'Type 1'),
	Venue('2', 'Venue 2', 'Location 2', 200, 'Type 2'),
	Venue('3', 'Venue 3', 'Location 3', 300, 'Type 3')
]

def search_venues(capacity, type):
	return [venue for venue in venues if venue.capacity >= capacity and venue.type == type]

def book_venue(id):
	for venue in venues:
		if venue.id == id:
			return venue.book_venue()
	return False
