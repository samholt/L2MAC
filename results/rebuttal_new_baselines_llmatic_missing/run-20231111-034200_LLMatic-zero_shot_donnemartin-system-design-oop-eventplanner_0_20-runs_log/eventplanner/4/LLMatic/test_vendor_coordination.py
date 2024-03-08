import pytest
import vendor_coordination


def test_vendor_creation():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', [])
	assert vendor.name == 'Test Vendor'
	assert vendor.service_type == 'Catering'
	assert vendor.reviews == []


def test_view_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', [])
	vendor_coordination.mock_database['1'] = vendor
	assert vendor_coordination.view_vendor('1') == vendor


def test_compare_vendors():
	vendor1 = vendor_coordination.Vendor('Test Vendor 1', 'Catering', [])
	vendor2 = vendor_coordination.Vendor('Test Vendor 2', 'Decor', [])
	vendor_coordination.mock_database['1'] = vendor1
	vendor_coordination.mock_database['2'] = vendor2
	assert vendor_coordination.compare_vendors('1', '2') == (vendor1, vendor2)


def test_send_message_to_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', [])
	vendor_coordination.mock_database['1'] = vendor
	assert vendor_coordination.send_message_to_vendor('1', 'Hello') == 'Message sent to Test Vendor: Hello'
