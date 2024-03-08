import pytest
from venues import Venue

def test_venue_search_and_booking():
	venue = Venue()
	venue.add_venue('1', 'Location1', 100, 'Type1')
	venue.add_venue('2', 'Location2', 200, 'Type2')
	venue.add_venue('3', 'Location3', 300, 'Type3')

	assert venue.search_venues('Location1') == ['1']
	assert venue.search_venues(capacity=250) == ['3']
	assert venue.search_venues(type='Type2') == ['2']
	assert venue.search_venues('Location3', 300, 'Type3') == ['3']

	assert venue.book_venue('1') == True
	assert venue.book_venue('1') == False
	assert venue.book_venue('4') == False
