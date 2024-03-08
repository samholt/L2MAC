import pytest
from vendor_coordination import Vendor, add_vendor_to_db, get_vendor_from_db, get_all_vendors_from_db


def test_vendor_creation():
	vendor = Vendor('Test Vendor', 'Catering', ['Good service', 'Delicious food'])
	assert vendor.name == 'Test Vendor'
	assert vendor.service_type == 'Catering'
	assert vendor.reviews == ['Good service', 'Delicious food']


def test_vendor_profile_viewing():
	vendor = Vendor('Test Vendor', 'Catering', ['Good service', 'Delicious food'])
	profile = vendor.view_profile()
	assert profile['name'] == 'Test Vendor'
	assert profile['service_type'] == 'Catering'
	assert profile['reviews'] == ['Good service', 'Delicious food']


def test_vendor_comparison():
	vendor1 = Vendor('Vendor 1', 'Catering', ['Good service'])
	vendor2 = Vendor('Vendor 2', 'Catering', ['Delicious food'])
	vendor3 = Vendor('Vendor 3', 'Photography', ['Great photos'])
	assert vendor1.compare_to(vendor2) == True
	assert vendor1.compare_to(vendor3) == False


def test_vendor_messaging():
	vendor = Vendor('Test Vendor', 'Catering', ['Good service', 'Delicious food'])
	message = vendor.send_message('Hello')
	assert message == 'Message sent to Test Vendor: Hello'


def test_vendor_database_functions():
	vendor = Vendor('Test Vendor', 'Catering', ['Good service', 'Delicious food'])
	add_vendor_to_db(vendor)
	retrieved_vendor = get_vendor_from_db('Test Vendor')
	assert retrieved_vendor == vendor
	all_vendors = get_all_vendors_from_db()
	assert all_vendors == [vendor]
