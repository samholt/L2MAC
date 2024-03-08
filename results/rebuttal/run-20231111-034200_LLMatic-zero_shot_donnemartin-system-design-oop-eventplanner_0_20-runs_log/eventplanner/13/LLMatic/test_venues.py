import pytest
from venues import Venue

@pytest.fixture

def venue_manager():
	return Venue()

def test_add_venue(venue_manager):
	venue_manager.add_venue('v1', 'Location 1', 100, 'Type 1')
	assert 'v1' in venue_manager.venues

def test_search_venues(venue_manager):
	venue_manager.add_venue('v1', 'Location 1', 100, 'Type 1')
	venue_manager.add_venue('v2', 'Location 2', 200, 'Type 2')
	results = venue_manager.search_venues(location='Location 1')
	assert len(results) == 1
	assert 'v1' in results[0]

def test_book_venue(venue_manager):
	venue_manager.add_venue('v1', 'Location 1', 100, 'Type 1')
	assert venue_manager.book_venue('v1')
	assert not venue_manager.book_venue('v1')
