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

@pytest.mark.parametrize('event', [
	Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Hawaiian', color_scheme='Blue and White'),
	Event(id=2, type='Wedding', date='2023-01-01', time='12:00', theme='Classic', color_scheme='White and Gold')
])
def test_create_event(client, reset_db, event):
	response = client.post('/event', json=event.__dict__)
	assert response.status_code == 201
	assert app.DB['events'][-1] == event

@pytest.mark.parametrize('venue', [
	Venue(id=1, location='New York', capacity=100, type='Hall'),
	Venue(id=2, location='Los Angeles', capacity=200, type='Outdoor')
])
def test_create_venue(client, reset_db, venue):
	response = client.post('/venue', json=venue.__dict__)
	assert response.status_code == 201
	assert app.DB['venues'][-1] == venue

@pytest.mark.parametrize('guest', [
	Guest(id=1, name='John Doe', email='johndoe@example.com'),
	Guest(id=2, name='Jane Doe', email='janedoe@example.com')
])
def test_create_guest(client, reset_db, guest):
	response = client.post('/guest', json=guest.__dict__)
	assert response.status_code == 201
	assert app.DB['guests'][-1] == guest

@pytest.mark.parametrize('vendor', [
	Vendor(id=1, name='Catering Co.', type='Catering', reviews=[]),
	Vendor(id=2, name='Decor Inc.', type='Decoration', reviews=[])
])
def test_create_vendor(client, reset_db, vendor):
	response = client.post('/vendor', json=vendor.__dict__)
	assert response.status_code == 201
	assert app.DB['vendors'][-1] == vendor
