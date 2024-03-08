class Venue:
	def __init__(self, id, name, location, capacity):
		self.id = id
		self.name = name
		self.location = location
		self.capacity = capacity
		self.booked = False

	def book_venue(self):
		self.booked = True

	def view_venue(self):
		return {'id': self.id, 'name': self.name, 'location': self.location, 'capacity': self.capacity, 'booked': self.booked}
