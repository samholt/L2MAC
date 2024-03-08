import pytest
from venues import Venue

def test_add_venue():
	venue = Venue()
	result = venue.add_venue('1', 'Test Venue', 'Test Location')
	assert result == {'name': 'Test Venue', 'location': 'Test Location'}

def test_get_venue():
	venue = Venue()
	venue.add_venue('1', 'Test Venue', 'Test Location')
	result = venue.get_venue('1')
	assert result == {'name': 'Test Venue', 'location': 'Test Location'}

def test_search_venues():
	venue = Venue()
	venue.add_venue('1', 'Test Venue', 'Test Location')
	result = venue.search_venues('Test')
	assert result == {'1': {'name': 'Test Venue', 'location': 'Test Location'}}

def test_book_venue():
	venue = Venue()
	venue.add_venue('1', 'Test Venue', 'Test Location')
	result = venue.book_venue('1')
	assert result == {'name': 'Test Venue', 'location': 'Test Location', 'booked': True}
