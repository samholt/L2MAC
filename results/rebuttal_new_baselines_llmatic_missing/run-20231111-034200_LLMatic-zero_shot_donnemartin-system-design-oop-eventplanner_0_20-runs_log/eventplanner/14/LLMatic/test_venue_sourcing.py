import venue_sourcing

def test_search_venues():
	venues = venue_sourcing.search_venues(200, 'Type 2')
	assert len(venues) == 1
	assert venues[0].name == 'Venue 2'

def test_book_venue():
	assert venue_sourcing.book_venue('1') == True
	assert venue_sourcing.book_venue('1') == False

def test_get_location():
	assert venue_sourcing.venues[0].get_location() == 'Location 1'
