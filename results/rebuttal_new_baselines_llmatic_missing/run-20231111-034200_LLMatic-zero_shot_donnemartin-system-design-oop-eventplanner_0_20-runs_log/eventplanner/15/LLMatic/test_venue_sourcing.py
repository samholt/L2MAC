import venue_sourcing

venue = venue_sourcing.Venue('Test Venue', 'Test Location')

def test_venue_search():
	assert venue.search_venue('Test Venue') == True
	assert venue.search_venue('Wrong Venue') == False

def test_venue_booking():
	assert venue.book_venue() == True
	assert venue.book_venue() == False

def test_venue_location():
	assert venue.get_location() == 'Test Location'
