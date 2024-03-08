import pytest
import venue_sourcing
from venue_sourcing import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_get_venues(client):
	response = client.get('/venues')
	assert response.status_code == 200


def test_add_venue(client):
	response = client.post('/venues', json={'name': 'Test Venue', 'location': 'Test Location'})
	assert response.status_code == 201


def test_book_venue(client):
	response = client.put('/venues/1', json={'booked': True})
	assert response.status_code == 200
