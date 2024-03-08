import pytest
from venues import Venue

def test_add_venue():
	venue = Venue()
	response = venue.add_venue('1', 'Venue 1', 'Location 1')
	assert response == {'status': 'success', 'message': 'Venue added successfully'}


def test_search_venue():
	venue = Venue()
	venue.add_venue('1', 'Venue 1', 'Location 1')
	response = venue.search_venue('Venue 1')
	assert response == {'status': 'success', 'venue': {'name': 'Venue 1', 'location': 'Location 1'}}


def test_get_venue_location():
	venue = Venue()
	venue.add_venue('1', 'Venue 1', 'Location 1')
	response = venue.get_venue_location('1')
	assert response == {'status': 'success', 'location': 'Location 1'}


def test_book_venue():
	venue = Venue()
	venue.add_venue('1', 'Venue 1', 'Location 1')
	response = venue.book_venue('1')
	assert response == {'status': 'success', 'message': 'Venue booked successfully'}
