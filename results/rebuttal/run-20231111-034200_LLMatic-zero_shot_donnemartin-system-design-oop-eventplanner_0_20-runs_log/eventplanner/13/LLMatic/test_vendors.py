import pytest
from vendors import Vendor

vendor_manager = Vendor()

def test_add_vendor():
	vendor_manager.add_vendor('1', {'name': 'Vendor 1', 'reviews': [], 'messages': []})
	assert vendor_manager.view_vendor('1') == {'name': 'Vendor 1', 'reviews': [], 'messages': []}

def test_view_vendor():
	assert vendor_manager.view_vendor('1') == {'name': 'Vendor 1', 'reviews': [], 'messages': []}

def test_compare_vendors():
	vendor_manager.add_vendor('2', {'name': 'Vendor 2', 'reviews': [], 'messages': []})
	assert vendor_manager.compare_vendors('1', '2') == ({'name': 'Vendor 1', 'reviews': [], 'messages': []}, {'name': 'Vendor 2', 'reviews': [], 'messages': []})

def test_message_vendor():
	assert vendor_manager.message_vendor('1', 'Hello') == True
	assert vendor_manager.view_vendor('1') == {'name': 'Vendor 1', 'reviews': [], 'messages': ['Hello']}
