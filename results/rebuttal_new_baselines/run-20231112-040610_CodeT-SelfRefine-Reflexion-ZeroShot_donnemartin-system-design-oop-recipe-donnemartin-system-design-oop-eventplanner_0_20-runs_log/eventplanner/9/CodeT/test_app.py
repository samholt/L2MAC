import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {'events': [], 'venues': [], 'guests': [], 'vendors': []}

@pytest.mark.usefixtures('reset_db')
def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Hawaiian', 'color_scheme': 'Blue and White'})
	assert response.status_code == 201
	assert len(app.DB['events']) == 1
	assert isinstance(app.DB['events'][0], Event)

@pytest.mark.usefixtures('reset_db')
def test_create_venue(client):
	response = client.post('/venue', json={'id': 1, 'location': 'New York', 'capacity': 100, 'type': 'Outdoor'})
	assert response.status_code == 201
	assert len(app.DB['venues']) == 1
	assert isinstance(app.DB['venues'][0], Venue)

@pytest.mark.usefixtures('reset_db')
def test_create_guest(client):
	response = client.post('/guest', json={'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'})
	assert response.status_code == 201
	assert len(app.DB['guests']) == 1
	assert isinstance(app.DB['guests'][0], Guest)

@pytest.mark.usefixtures('reset_db')
def test_create_vendor(client):
	response = client.post('/vendor', json={'id': 1, 'name': 'Catering Co.', 'type': 'Catering', 'reviews': []})
	assert response.status_code == 201
	assert len(app.DB['vendors']) == 1
	assert isinstance(app.DB['vendors'][0], Vendor)
