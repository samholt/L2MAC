import pytest
from vendors import Vendor

def test_add_vendor():
	vendor = Vendor()
	vendor.add_vendor('1', {'name': 'Vendor 1', 'rating': 5})
	assert vendor.get_vendor('1') == {'name': 'Vendor 1', 'rating': 5}

def test_get_vendor():
	vendor = Vendor()
	vendor.add_vendor('1', {'name': 'Vendor 1', 'rating': 5})
	assert vendor.get_vendor('1') == {'name': 'Vendor 1', 'rating': 5}

def test_get_all_vendors():
	vendor = Vendor()
	vendor.add_vendor('1', {'name': 'Vendor 1', 'rating': 5})
	vendor.add_vendor('2', {'name': 'Vendor 2', 'rating': 4})
	assert vendor.get_all_vendors() == {'1': {'name': 'Vendor 1', 'rating': 5}, '2': {'name': 'Vendor 2', 'rating': 4}}

def test_delete_vendor():
	vendor = Vendor()
	vendor.add_vendor('1', {'name': 'Vendor 1', 'rating': 5})
	vendor.delete_vendor('1')
	assert vendor.get_vendor('1') == None

def test_update_vendor():
	vendor = Vendor()
	vendor.add_vendor('1', {'name': 'Vendor 1', 'rating': 5})
	vendor.update_vendor('1', {'name': 'Vendor 1', 'rating': 4})
	assert vendor.get_vendor('1') == {'name': 'Vendor 1', 'rating': 4}
