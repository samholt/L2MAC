import pytest
from venue_sourcing import VenueSourcing

@pytest.fixture

def venue_sourcing():
	vs = VenueSourcing()
	vs.add_venue('1', {'name': 'Venue 1', 'location': 'Location 1', 'capacity': 100, 'booked': False})
	vs.add_venue('2', {'name': 'Venue 2', 'location': 'Location 2', 'capacity': 200, 'booked': False})
	return vs


def test_search_venues(venue_sourcing):
	results = venue_sourcing.search_venues({'location': 'Location 1'})
	assert len(results) == 1
	assert results[0][0] == '1'


def test_book_venue(venue_sourcing):
	assert venue_sourcing.book_venue('1') == True
	assert venue_sourcing.book_venue('3') == False
