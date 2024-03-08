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
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}


def test_update_event(client):
	client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Wedding', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}


def test_create_venue(client):
	response = client.post('/venue', json={'id': 1, 'name': 'Grand Hall', 'location': '123 Main St', 'capacity': 200, 'type': 'Indoor'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'Grand Hall', 'location': '123 Main St', 'capacity': 200, 'type': 'Indoor'}


def test_update_venue(client):
	client.post('/venue', json={'id': 1, 'name': 'Grand Hall', 'location': '123 Main St', 'capacity': 200, 'type': 'Indoor'})
	response = client.put('/venue/1', json={'name': 'Great Hall'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'name': 'Great Hall', 'location': '123 Main St', 'capacity': 200, 'type': 'Indoor'}


def test_create_guest(client):
	response = client.post('/guest', json={'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'}


def test_update_guest(client):
	client.post('/guest', json={'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'})
	response = client.put('/guest/1', json={'name': 'Jane Doe'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'name': 'Jane Doe', 'email': 'johndoe@example.com'}


def test_create_vendor(client):
	response = client.post('/vendor', json={'id': 1, 'name': 'Best Catering', 'type': 'Catering', 'reviews': ['Great service!', 'Delicious food!']})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'Best Catering', 'type': 'Catering', 'reviews': ['Great service!', 'Delicious food!']}


def test_update_vendor(client):
	client.post('/vendor', json={'id': 1, 'name': 'Best Catering', 'type': 'Catering', 'reviews': ['Great service!', 'Delicious food!']})
	response = client.put('/vendor/1', json={'name': 'Super Catering'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'name': 'Super Catering', 'type': 'Catering', 'reviews': ['Great service!', 'Delicious food!']}
