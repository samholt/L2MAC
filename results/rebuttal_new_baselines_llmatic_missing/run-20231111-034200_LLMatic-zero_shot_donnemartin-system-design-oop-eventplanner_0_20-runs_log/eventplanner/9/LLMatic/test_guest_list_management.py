import pytest
import guest_list_management
from database import Database

@pytest.fixture
def client():
	guest_list_management.app.config['TESTING'] = True
	with guest_list_management.app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def setup_teardown():
	# Setup: Initialize Database
	guest_list_management.db = Database()
	# Teardown: Reset Database
	yield
	guest_list_management.db = Database()

def test_create_guest_list(client):
	guest_list = {'name': 'Test', 'guests': ['John', 'Jane']}
	response = client.post('/create_guest_list', json=guest_list)
	assert response.status_code == 201
	assert len(guest_list_management.db.get_all('guest_lists')) == 1

def test_get_guest_list(client):
	guest_list = {'name': 'Test', 'guests': ['John', 'Jane']}
	id = guest_list_management.db.insert('guest_lists', guest_list)
	response = client.get('/get_guest_list/'+str(id))
	assert response.status_code == 200
	assert response.get_json() is not None

def test_update_guest_list(client):
	guest_list = {'name': 'Test', 'guests': ['John', 'Jane']}
	id = guest_list_management.db.insert('guest_lists', guest_list)
	guest_list = {'name': 'Test Updated', 'guests': ['John', 'Jane', 'Doe']}
	response = client.put('/update_guest_list/'+str(id), json=guest_list)
	assert response.status_code == 200
	updated_guest_list = guest_list_management.db.get('guest_lists', id)
	assert updated_guest_list['name'] == 'Test Updated'

def test_delete_guest_list(client):
	guest_list = {'name': 'Test', 'guests': ['John', 'Jane']}
	id = guest_list_management.db.insert('guest_lists', guest_list)
	response = client.delete('/delete_guest_list/'+str(id))
	assert response.status_code == 200
	assert len(guest_list_management.db.get_all('guest_lists')) == 0

def test_rsvp(client):
	guest_list = {'name': 'Test', 'guests': ['John', 'Jane'], 'rsvp': []}
	id = guest_list_management.db.insert('guest_lists', guest_list)
	response = client.put('/rsvp/'+str(id), json={'rsvp': ['John', 'Jane']})
	assert response.status_code == 200
	updated_guest_list = guest_list_management.db.get('guest_lists', id)
	assert 'John' in updated_guest_list['rsvp']
	assert 'Jane' in updated_guest_list['rsvp']
