import pytest
import vendor_coordination as vc


def test_connect_vendor():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.post('/connect_vendor', json={'vendor_id': '1', 'name': 'Vendor 1', 'reviews': [], 'messages': []})
	assert response.status_code == 200
	assert vc.vendors['1']['name'] == 'Vendor 1'


def test_view_vendor():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.get('/view_vendor?vendor_id=1')
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Vendor 1'


def test_compare_vendors():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.get('/compare_vendors?vendor_ids=1&vendor_ids=2')
	assert response.status_code == 200
	assert 'Vendor 1' in [vendor.get('name') if isinstance(vendor, dict) else vendor for vendor in response.get_json().values()]


def test_message_vendor():
	vc.app.testing = True
	client = vc.app.test_client()
	response = client.post('/message_vendor', json={'vendor_id': '1', 'message': 'Hello'})
	assert response.status_code == 200
	assert 'Hello' in vc.vendors['1']['messages']
