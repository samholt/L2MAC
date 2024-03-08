class Venue:
	def __init__(self):
		self.venues = {}

	def add_venue(self, venue_id, venue_name, venue_location):
		self.venues[venue_id] = {'name': venue_name, 'location': venue_location}
		return {'status': 'success', 'message': 'Venue added successfully'}

	def search_venue(self, venue_name):
		for venue_id, venue_info in self.venues.items():
			if venue_info['name'] == venue_name:
				return {'status': 'success', 'venue': venue_info}
		return {'status': 'failure', 'message': 'Venue not found'}

	def get_venue_location(self, venue_id):
		if venue_id in self.venues:
			return {'status': 'success', 'location': self.venues[venue_id]['location']}
		return {'status': 'failure', 'message': 'Venue not found'}

	def book_venue(self, venue_id):
		if venue_id in self.venues:
			return {'status': 'success', 'message': 'Venue booked successfully'}
		return {'status': 'failure', 'message': 'Venue not found'}
