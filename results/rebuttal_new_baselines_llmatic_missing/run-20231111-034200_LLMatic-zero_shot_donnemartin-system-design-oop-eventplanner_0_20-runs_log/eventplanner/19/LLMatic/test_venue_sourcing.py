import pytest
from venue_sourcing import VenueSourcing


def test_venue_sourcing():
	venue_sourcing = VenueSourcing()
	venue_sourcing.add_venue(1, 'Venue 1', 'Location 1', 100, 'Type 1')
	venue_sourcing.add_venue(2, 'Venue 2', 'Location 2', 200, 'Type 2')
	venue_sourcing.add_venue(3, 'Venue 3', 'Location 3', 300, 'Type 3')

	# Test search by location
	results = venue_sourcing.search_venues(location='Location 1')
	assert len(results) == 1
	assert results[0].name == 'Venue 1'

	# Test search by capacity
	results = venue_sourcing.search_venues(capacity=200)
	assert len(results) == 2
	assert results[0].name == 'Venue 2'
	assert results[1].name == 'Venue 3'

	# Test search by type
	results = venue_sourcing.search_venues(type='Type 3')
	assert len(results) == 1
	assert results[0].name == 'Venue 3'

	# Test booking
	assert venue_sourcing.book_venue(1) == True
	assert venue_sourcing.book_venue(4) == False
