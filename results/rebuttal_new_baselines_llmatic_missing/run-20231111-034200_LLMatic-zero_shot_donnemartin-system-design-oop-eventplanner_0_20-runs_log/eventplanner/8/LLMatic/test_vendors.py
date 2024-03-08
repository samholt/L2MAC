from vendors import Vendor
from database import Database

def test_vendor():
	vendor1 = Vendor(1, 'Vendor 1', 'Profile 1', ['Good', 'Excellent'])
	vendor2 = Vendor(2, 'Vendor 2', 'Profile 2', ['Bad', 'Poor'])
	db = Database()
	db.add_vendor(vendor1)
	db.add_vendor(vendor2)

	# Test viewing vendor profile
	assert db.get_vendor(1) == 'Profile 1'
	assert db.get_vendor(2) == 'Profile 2'

	# Test comparing vendor profiles
	assert vendor1.compare_profiles(vendor2) == False

	# Test viewing vendor reviews
	assert vendor1.view_reviews() == ['Good', 'Excellent']
	assert vendor2.view_reviews() == ['Bad', 'Poor']

	# Test sending and viewing messages
	db.send_message_to_vendor(1, 'Hello')
	assert vendor1.view_messages() == ['Hello']
