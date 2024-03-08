import pytest
from vendor_coordination import VendorCoordination


def test_vendor_coordination():
	vc = VendorCoordination()
	vc.add_vendor('v1', {'name': 'Vendor 1', 'rating': 4.5})
	vc.add_vendor('v2', {'name': 'Vendor 2', 'rating': 3.8})
	assert vc.view_vendor('v1') == {'name': 'Vendor 1', 'rating': 4.5}
	assert vc.view_vendor('v3') == 'Vendor not found'
	assert vc.compare_vendors('v1', 'v2') == ({'name': 'Vendor 1', 'rating': 4.5}, {'name': 'Vendor 2', 'rating': 3.8})
	vc.send_message('v1', 'Hello Vendor 1')
	vc.send_message('v1', 'How are you?')
	assert vc.view_messages('v1') == ['Hello Vendor 1', 'How are you?']
	assert vc.view_messages('v2') == 'No messages found'
