import venue_sourcing


def test_search_venue():
	venue_sourcing.mock_database = {1: venue_sourcing.Venue(1, 'Location1', 100, 'Type1'), 2: venue_sourcing.Venue(2, 'Location2', 200, 'Type2')}
	assert len(venue_sourcing.search_venue('Location1', 50, 'Type1')) == 1
	assert len(venue_sourcing.search_venue('Location2', 300, 'Type2')) == 0


def test_book_venue():
	venue_sourcing.mock_database = {1: venue_sourcing.Venue(1, 'Location1', 100, 'Type1'), 2: venue_sourcing.Venue(2, 'Location2', 200, 'Type2')}
	assert venue_sourcing.book_venue(1) == True
	assert venue_sourcing.book_venue(1) == False
	assert venue_sourcing.book_venue(3) == False
