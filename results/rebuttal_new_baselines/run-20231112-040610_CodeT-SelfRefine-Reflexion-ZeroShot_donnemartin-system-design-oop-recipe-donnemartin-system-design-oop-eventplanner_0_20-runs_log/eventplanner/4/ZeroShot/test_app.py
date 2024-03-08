import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Hawaiian', 'color_scheme': 'Blue and White'})
	assert response.status_code == 201
	assert app.DB['events'][0] == Event(1, 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')


def test_create_venue(client):
	response = client.post('/venue', json={'id': 1, 'location': 'New York', 'capacity': 100, 'type': 'Outdoor'})
	assert response.status_code == 201
	assert app.DB['venues'][0] == Venue(1, 'New York', 100, 'Outdoor')


def test_create_guest(client):
	response = client.post('/guest', json={'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'})
	assert response.status_code == 201
	assert app.DB['guests'][0] == Guest(1, 'John Doe', 'johndoe@example.com')


def test_create_vendor(client):
	response = client.post('/vendor', json={'id': 1, 'name': 'ABC Catering', 'type': 'Catering', 'reviews': ['Excellent service', 'Great food']})
	assert response.status_code == 201
	assert app.DB['vendors'][0] == Vendor(1, 'ABC Catering', 'Catering', ['Excellent service', 'Great food'])
