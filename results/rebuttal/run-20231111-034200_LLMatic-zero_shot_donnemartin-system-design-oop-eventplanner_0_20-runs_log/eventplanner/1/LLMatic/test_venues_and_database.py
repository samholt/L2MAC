import pytest
from venues import Venue
from database import Database

def test_venue_creation():
	venue = Venue('1', 'Location', 100, 'Type')
	assert venue.venue_id == '1'
	assert venue.location == 'Location'
	assert venue.capacity == 100
	assert venue.venue_type == 'Type'
	assert venue.booked == False

def test_venue_booking():
	venue = Venue('1', 'Location', 100, 'Type')
	assert venue.book_venue() == True
	assert venue.booked == True
	assert venue.book_venue() == False

def test_venue_search():
	venue = Venue('1', 'Location', 100, 'Type')
	assert venue.search_venue('Location', 100, 'Type') == True
	assert venue.search_venue('Wrong Location', 100, 'Type') == False

def test_database_venue_storage():
	db = Database()
	venue = Venue('1', 'Location', 100, 'Type')
	db.add_venue('1', venue)
	assert db.get_venue('1') == venue
	assert db.get_venue('2') == None
