import pytest
from venue_sourcing import Venue, VenueSourcing


def test_venue_creation():
	venue = Venue('Test Venue', 'Test Location', 100, 'Conference')
	assert venue.get_venue_details() == {'name': 'Test Venue', 'location': 'Test Location', 'capacity': 100, 'type': 'Conference', 'is_booked': False}


def test_venue_booking():
	venue = Venue('Test Venue', 'Test Location', 100, 'Conference')
	assert venue.book_venue() == True
	assert venue.get_venue_details() == {'name': 'Test Venue', 'location': 'Test Location', 'capacity': 100, 'type': 'Conference', 'is_booked': True}


def test_venue_sourcing():
	venue_sourcing = VenueSourcing()
	venue_sourcing.add_venue('Test Venue', 'Test Location', 100, 'Conference')
	venue_sourcing.add_venue('Test Venue 2', 'Test Location 2', 50, 'Meeting')

	available_venues = venue_sourcing.search_venues(50, 'Meeting')
	assert len(available_venues) == 1
	assert available_venues[0].get_venue_details() == {'name': 'Test Venue 2', 'location': 'Test Location 2', 'capacity': 50, 'type': 'Meeting', 'is_booked': False}

	assert venue_sourcing.book_venue('Test Venue 2') == True
	assert venue_sourcing.book_venue('Test Venue 2') == False
