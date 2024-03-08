import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert app.DB['events'][0].type == 'Birthday'


def test_create_venue(client):
	response = client.post('/venue', json={'id': 1, 'location': 'New York', 'capacity': 100, 'type': 'Hall'})
	assert response.status_code == 201
	assert app.DB['venues'][0].location == 'New York'


def test_create_guest(client):
	response = client.post('/guest', json={'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'})
	assert response.status_code == 201
	assert app.DB['guests'][0].name == 'John Doe'


def test_create_vendor(client):
	response = client.post('/vendor', json={'id': 1, 'name': 'Catering Co.', 'type': 'Catering', 'reviews': ['Great service', 'Delicious food']})
	assert response.status_code == 201
	assert app.DB['vendors'][0].name == 'Catering Co.'}
