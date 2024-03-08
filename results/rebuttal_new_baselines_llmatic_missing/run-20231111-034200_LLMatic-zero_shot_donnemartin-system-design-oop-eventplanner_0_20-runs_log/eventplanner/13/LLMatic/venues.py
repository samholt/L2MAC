class Venue:
	def __init__(self):
		self.venues = {}

	def add_venue(self, venue_id, location, capacity, venue_type):
		self.venues[venue_id] = {'location': location, 'capacity': capacity, 'type': venue_type, 'booked': False}

	def search_venues(self, location=None, capacity=None, venue_type=None):
		results = []
		for venue_id, details in self.venues.items():
			if location and details['location'] != location:
				continue
			if capacity and details['capacity'] < capacity:
				continue
			if venue_type and details['type'] != venue_type:
				continue
			results.append({venue_id: details})
		return results

	def book_venue(self, venue_id):
		if self.venues[venue_id]['booked']:
			return False
		self.venues[venue_id]['booked'] = True
		return True
