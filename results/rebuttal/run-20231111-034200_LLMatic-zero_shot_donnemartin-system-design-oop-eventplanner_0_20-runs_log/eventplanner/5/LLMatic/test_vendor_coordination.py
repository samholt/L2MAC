import pytest
from vendor_coordination import Vendor

def test_vendor():
	vendor1 = Vendor({'name': 'Vendor1', 'location': 'Location1'}, 4.5)
	vendor2 = Vendor({'name': 'Vendor2', 'location': 'Location2'}, 4.0)

	assert vendor1.view_profile() == {'name': 'Vendor1', 'location': 'Location1'}
	assert vendor1.compare_vendors(vendor2) == True
	assert vendor1.communicate('Hello') == 'Sending message: Hello to Vendor1'
