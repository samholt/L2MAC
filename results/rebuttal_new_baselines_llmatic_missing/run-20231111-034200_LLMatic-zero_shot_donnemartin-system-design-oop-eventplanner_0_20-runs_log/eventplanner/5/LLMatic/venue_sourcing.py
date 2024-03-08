class Venue:
	def __init__(self, id, location, capacity, type):
		self.id = id
		self.location = location
		self.capacity = capacity
		self.type = type
		self.booked = False

	def book(self):
		if not self.booked:
			self.booked = True
			return True
		return False

	def is_available(self):
		return not self.booked


venues = [
	Venue('1', 'New York', 100, 'Conference Hall'),
	Venue('2', 'Los Angeles', 200, 'Banquet Hall'),
	Venue('3', 'Chicago', 150, 'Auditorium')
]

def search_venues(location, capacity, type):
	return [venue for venue in venues if venue.location == location and venue.capacity >= capacity and venue.type == type and venue.is_available()]

def book_venue(id):
	for venue in venues:
		if venue.id == id:
			return venue.book()
	return False
