from venues import Venue
from database import Database

def test_venue():
	db = Database()
	venue = Venue(1, 'Test Venue', 'Test Location', 100)
	db.add_venue(venue)
	assert db.get_venue(1) == {'id': 1, 'name': 'Test Venue', 'location': 'Test Location', 'capacity': 100, 'booked': False}
	db.book_venue(1)
	assert db.get_venue(1) == {'id': 1, 'name': 'Test Venue', 'location': 'Test Location', 'capacity': 100, 'booked': True}
