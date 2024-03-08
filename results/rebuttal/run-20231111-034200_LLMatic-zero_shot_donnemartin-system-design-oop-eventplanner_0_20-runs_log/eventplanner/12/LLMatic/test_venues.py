import pytest
from venues import Venue, add_venue, get_venue, search_venues, book_venue


def test_venue_creation():
	venue = Venue('1', 'New York', 100, 'Conference Hall')
	assert venue.id == '1'
	assert venue.location == 'New York'
	assert venue.capacity == 100
	assert venue.type == 'Conference Hall'
	assert not venue.booked


def test_add_and_get_venue():
	venue = Venue('1', 'New York', 100, 'Conference Hall')
	add_venue(venue)
	retrieved_venue = get_venue('1')
	assert retrieved_venue == venue


def test_search_venues():
	venue1 = Venue('1', 'New York', 100, 'Conference Hall')
	venue2 = Venue('2', 'New York', 200, 'Banquet Hall')
	add_venue(venue1)
	add_venue(venue2)
	search_results = search_venues('New York', 150, 'Banquet Hall')
	assert len(search_results) == 1
	assert search_results[0] == venue2


def test_book_venue():
	venue = Venue('1', 'New York', 100, 'Conference Hall')
	add_venue(venue)
	assert not venue.booked
	book_venue('1')
	assert venue.booked
