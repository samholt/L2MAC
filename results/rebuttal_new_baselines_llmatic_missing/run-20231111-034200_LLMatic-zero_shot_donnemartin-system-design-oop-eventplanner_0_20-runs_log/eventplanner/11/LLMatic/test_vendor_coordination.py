import pytest
from vendor_coordination import VendorCoordination


def test_add_get_vendor():
	vc = VendorCoordination()
	vc.add_vendor('v1', {'name': 'Vendor 1', 'rating': 4.5, 'messages': []})
	vendor = vc.get_vendor('v1')
	assert vendor['name'] == 'Vendor 1'
	assert vendor['rating'] == 4.5


def test_compare_vendors():
	vc = VendorCoordination()
	vc.add_vendor('v1', {'name': 'Vendor 1', 'rating': 4.5, 'messages': []})
	vc.add_vendor('v2', {'name': 'Vendor 2', 'rating': 3.5, 'messages': []})
	assert vc.compare_vendors('v1', 'v2') == 1.0


def test_send_message():
	vc = VendorCoordination()
	vc.add_vendor('v1', {'name': 'Vendor 1', 'rating': 4.5, 'messages': []})
	assert vc.send_message('v1', 'Hello') == True
	assert 'Hello' in vc.get_vendor('v1')['messages']
