class VenueSourcing:
	def __init__(self):
		self.venues = {}

	def add_venue(self, venue_id, venue_details):
		self.venues[venue_id] = venue_details

	def search_venues(self, search_criteria):
		results = []
		for venue_id, venue_details in self.venues.items():
			if all(item in venue_details.items() for item in search_criteria.items()):
				results.append((venue_id, venue_details))
		return results

	def book_venue(self, venue_id):
		if venue_id in self.venues:
			self.venues[venue_id]['booked'] = True
			return True
		return False
