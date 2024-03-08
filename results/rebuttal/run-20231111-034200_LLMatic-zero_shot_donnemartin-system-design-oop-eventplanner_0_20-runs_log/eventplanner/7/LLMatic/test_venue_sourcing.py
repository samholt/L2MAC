import pytest
from venue_sourcing import app, db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_add_venue(client):
	response = client.post('/add_venue', json={'venue_id': '1', 'venue_details': {'name': 'Test Venue', 'location': 'Test Location'}})
	assert response.status_code == 200
	assert db.get_venue('1') == {'name': 'Test Venue', 'location': 'Test Location'}


def test_get_venue(client):
	response = client.get('/get_venue/1')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test Venue', 'location': 'Test Location'}


def test_search_venues(client):
	response = client.get('/search_venues?search_term=Test')
	assert response.status_code == 200
	assert response.get_json() == {'1': {'name': 'Test Venue', 'location': 'Test Location'}}
