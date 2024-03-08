import pytest
from venue_sourcing import Venue, VenueSourcing


def test_venue_sourcing():
	venue_sourcing = VenueSourcing()
	venue1 = Venue('1', 'Location1', 100, 'Type1')
	venue2 = Venue('2', 'Location2', 200, 'Type2')
	venue_sourcing.add_venue(venue1)
	venue_sourcing.add_venue(venue2)

	assert venue_sourcing.search_venue('Location1', 50, 'Type1') == venue1
	assert venue_sourcing.search_venue('Location2', 300, 'Type2') == None
	assert venue_sourcing.search_venue('Location3', 50, 'Type1') == None

	assert venue_sourcing.book_venue('1') == True
	assert venue_sourcing.book_venue('1') == False
	assert venue_sourcing.book_venue('3') == False
