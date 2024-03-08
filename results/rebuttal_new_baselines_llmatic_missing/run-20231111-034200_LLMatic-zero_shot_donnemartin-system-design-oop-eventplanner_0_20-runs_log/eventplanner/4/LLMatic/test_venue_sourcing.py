import pytest
import venue_sourcing

def test_venue_sourcing():
	vs = venue_sourcing.VenueSourcing()
	vs.add_venue('1', 'Location 1', 100, 'Type 1')
	vs.add_venue('2', 'Location 2', 200, 'Type 2')
	vs.add_venue('3', 'Location 3', 300, 'Type 1')

	venue = vs.search_venue(150, 'Type 1')
	assert venue is not None
	assert venue.id == '3'

	venue = vs.search_venue(100, 'Type 1')
	assert venue is not None
	assert venue.id == '1'

	assert vs.book_venue('1') is True
	assert vs.book_venue('1') is False

	venue = vs.search_venue(100, 'Type 1')
	assert venue is None or venue.id != '1'

	venue = vs.search_venue(300, 'Type 1')
	assert venue is not None
	assert venue.id == '3'

	assert vs.book_venue('3') is True
	assert vs.book_venue('3') is False

	venue = vs.search_venue(200, 'Type 2')
	assert venue is not None
	assert venue.id == '2'

	assert vs.book_venue('2') is True
	assert vs.book_venue('2') is False

	venue = vs.search_venue(200, 'Type 2')
	assert venue is None or venue.id != '2'
