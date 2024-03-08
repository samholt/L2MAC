class Venue:
	def __init__(self):
		self.venues = {}

	def add_venue(self, venue_id, venue_name, venue_location):
		self.venues[venue_id] = {'name': venue_name, 'location': venue_location}
		return self.venues[venue_id]

	def get_venue(self, venue_id):
		return self.venues.get(venue_id, None)

	def search_venues(self, search_term):
		return {venue_id: venue for venue_id, venue in self.venues.items() if search_term in venue['name']}

	def book_venue(self, venue_id):
		venue = self.get_venue(venue_id)
		if venue:
			venue['booked'] = True
		return venue
