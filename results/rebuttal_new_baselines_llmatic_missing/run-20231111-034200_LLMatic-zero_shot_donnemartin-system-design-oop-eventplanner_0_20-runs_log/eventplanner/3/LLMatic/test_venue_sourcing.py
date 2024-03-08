import pytest
import venue_sourcing


def setup_module(module):
	venue_sourcing.venues = {
		1: venue_sourcing.Venue(1, 'Location 1', 100, 'Type 1'),
		2: venue_sourcing.Venue(2, 'Location 2', 200, 'Type 2')
	}


def test_find_venue():
	venue = venue_sourcing.find_venue('Location 1', 100, 'Type 1')
	assert venue is not None
	assert venue.id == 1


def test_book_venue():
	is_booked = venue_sourcing.book_venue(1)
	assert is_booked
	assert venue_sourcing.venues[1].is_booked
