import pytest
from vendors import Vendor
from database import Database

def test_vendor_creation():
	vendor = Vendor('Test Vendor', 'Catering', 'Profile description', ['Good service', 'Excellent food'])
	assert vendor.name == 'Test Vendor'
	assert vendor.service_type == 'Catering'
	assert vendor.profile == 'Profile description'
	assert vendor.reviews == ['Good service', 'Excellent food']

def test_vendor_viewing():
	vendor = Vendor('Test Vendor', 'Catering', 'Profile description', ['Good service', 'Excellent food'])
	assert vendor.view_vendor() == {'name': 'Test Vendor', 'service_type': 'Catering', 'profile': 'Profile description', 'reviews': ['Good service', 'Excellent food']}

def test_vendor_comparison():
	vendor1 = Vendor('Test Vendor 1', 'Catering', 'Profile description', ['Good service', 'Excellent food'])
	vendor2 = Vendor('Test Vendor 2', 'Photography', 'Profile description', ['Excellent shots', 'Professional service'])
	assert vendor1.compare_to(vendor2) == False

def test_vendor_messaging():
	vendor = Vendor('Test Vendor', 'Catering', 'Profile description', ['Good service', 'Excellent food'])
	assert vendor.send_message('Hello') == 'Message sent to Test Vendor: Hello'

def test_vendor_storage():
	db = Database()
	vendor = Vendor('Test Vendor', 'Catering', 'Profile description', ['Good service', 'Excellent food'])
	db.add_vendor('1', vendor)
	assert db.get_vendor('1') == vendor
