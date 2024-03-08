import pytest
import vendor_coordination


def test_add_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', 4.5)
	vendor_coordination.add_vendor(vendor)
	assert vendor_coordination.get_vendor('Test Vendor') == vendor


def test_remove_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', 4.5)
	vendor_coordination.add_vendor(vendor)
	vendor_coordination.remove_vendor('Test Vendor')
	assert vendor_coordination.get_vendor('Test Vendor') is None


def test_update_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', 4.5)
	vendor_coordination.add_vendor(vendor)
	new_vendor = vendor_coordination.Vendor('Test Vendor', 'Photography', 5.0)
	vendor_coordination.update_vendor('Test Vendor', new_vendor)
	assert vendor_coordination.get_vendor('Test Vendor') == new_vendor


def test_compare_vendors():
	vendor1 = vendor_coordination.Vendor('Vendor 1', 'Catering', 4.5)
	vendor2 = vendor_coordination.Vendor('Vendor 2', 'Photography', 5.0)
	assert vendor_coordination.compare_vendors(vendor1, vendor2) is False


def test_send_message_to_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', 'Catering', 4.5)
	vendor_coordination.add_vendor(vendor)
	assert vendor_coordination.send_message_to_vendor('Test Vendor', 'Hello') == 'Message sent to Test Vendor: Hello'
