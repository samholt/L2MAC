import pytest
import vendor_coordination as vc


def test_add_vendor():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.post('/vendors', json={'name': 'Test Vendor', 'rating': 5})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_get_vendors():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.get('/vendors')
	assert response.status_code == 200
	vendors = response.get_json()
	assert isinstance(vendors, list)


def test_get_vendor():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.post('/vendors', json={'name': 'Test Vendor', 'rating': 5})
	vendor_id = response.get_json()['id']
	response = client.get(f'/vendors/{vendor_id}')
	assert response.status_code == 200
	vendor = response.get_json()
	assert vendor['name'] == 'Test Vendor'
	assert vendor['rating'] == 5


def test_send_message():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.post('/vendors', json={'name': 'Test Vendor', 'rating': 5})
	vendor_id = response.get_json()['id']
	response = client.post(f'/vendors/{vendor_id}/messages', json={'content': 'Test message'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
