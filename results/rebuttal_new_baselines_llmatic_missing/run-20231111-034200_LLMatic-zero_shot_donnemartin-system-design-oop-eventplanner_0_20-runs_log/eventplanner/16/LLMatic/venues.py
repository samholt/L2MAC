class Venue:
	def __init__(self):
		self.venues = {}

	def add_venue(self, id, location, capacity, type):
		self.venues[id] = {'location': location, 'capacity': capacity, 'type': type, 'booked': False}

	def search_venues(self, location=None, capacity=None, type=None):
		results = []
		for id, venue in self.venues.items():
			if location and venue['location'] != location:
				continue
			if capacity and venue['capacity'] < capacity:
				continue
			if type and venue['type'] != type:
				continue
			results.append(id)
		return results

	def book_venue(self, id):
		if id in self.venues and not self.venues[id]['booked']:
			self.venues[id]['booked'] = True
			return True
		return False
