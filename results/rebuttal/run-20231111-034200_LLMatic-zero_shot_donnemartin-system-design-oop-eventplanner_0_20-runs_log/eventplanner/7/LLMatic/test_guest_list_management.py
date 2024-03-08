import pytest
import guest_list_management as glm

def test_create_guest_list():
	glm.app.testing = True
	client = glm.app.test_client()
	response = client.post('/create_guest_list', json={'guest_list_name': 'Test List'})
	assert response.status_code == 200
	assert glm.guest_lists['Test List'] == []

def test_add_guest():
	glm.app.testing = True
	client = glm.app.test_client()
	response = client.post('/add_guest', json={'guest_list_name': 'Test List', 'guest': {'name': 'John Doe', 'rsvp': 'No'}})
	assert response.status_code == 200
	assert glm.guest_lists['Test List'][0]['name'] == 'John Doe'

def test_get_guest_list():
	glm.app.testing = True
	client = glm.app.test_client()
	response = client.get('/get_guest_list', query_string={'guest_list_name': 'Test List'})
	assert response.status_code == 200
	assert response.get_json()['guest_list'][0]['name'] == 'John Doe'

def test_rsvp():
	glm.app.testing = True
	client = glm.app.test_client()
	response = client.post('/rsvp', json={'guest_list_name': 'Test List', 'guest': 'John Doe', 'status': 'Yes'})
	assert response.status_code == 200
	assert glm.guest_lists['Test List'][0]['rsvp'] == 'Yes'
