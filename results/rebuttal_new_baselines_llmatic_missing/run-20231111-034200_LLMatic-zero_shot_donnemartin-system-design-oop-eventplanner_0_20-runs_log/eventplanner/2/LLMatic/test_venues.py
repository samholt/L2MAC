import pytest
from venues import Venue

@pytest.fixture

def venue():
	return Venue()

def test_add_venue(venue):
	venue_info = venue.add_venue('1', 'Test Venue', 'Test Location')
	assert venue_info == {'name': 'Test Venue', 'location': 'Test Location'}

def test_get_venue(venue):
	venue.add_venue('1', 'Test Venue', 'Test Location')
	venue_info = venue.get_venue('1')
	assert venue_info == {'name': 'Test Venue', 'location': 'Test Location'}

def test_search_venues(venue):
	venue.add_venue('1', 'Test Venue', 'Test Location')
	search_results = venue.search_venues('Test')
	assert search_results == {'1': {'name': 'Test Venue', 'location': 'Test Location'}}

def test_book_venue(venue):
	venue.add_venue('1', 'Test Venue', 'Test Location')
	booking_info = venue.book_venue('1')
	assert booking_info == {'name': 'Test Venue', 'location': 'Test Location', 'booked': True}
