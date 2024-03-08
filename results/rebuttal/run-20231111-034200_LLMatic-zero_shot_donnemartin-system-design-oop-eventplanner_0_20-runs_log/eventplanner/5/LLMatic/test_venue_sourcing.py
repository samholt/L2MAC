import venue_sourcing

def test_search_venues():
	venues = venue_sourcing.search_venues('New York', 100, 'Conference Hall')
	assert len(venues) == 1
	assert venues[0].id == '1'

def test_book_venue():
	assert venue_sourcing.book_venue('1') == True
	assert venue_sourcing.venues[0].booked == True
	assert venue_sourcing.book_venue('1') == False
