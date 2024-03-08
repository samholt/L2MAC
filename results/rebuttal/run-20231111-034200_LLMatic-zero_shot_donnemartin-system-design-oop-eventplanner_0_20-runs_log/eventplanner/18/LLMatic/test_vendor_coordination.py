import pytest
from vendor_coordination import Vendor, MessagingSystem


def test_vendor():
	vendor1 = Vendor('Vendor1', 'Catering', ['Good', 'Excellent'])
	vendor2 = Vendor('Vendor2', 'Music', ['Average', 'Good'])
	assert vendor1.view_profile() == {'name': 'Vendor1', 'service_type': 'Catering', 'reviews': ['Good', 'Excellent']}
	assert vendor2.view_profile() == {'name': 'Vendor2', 'service_type': 'Music', 'reviews': ['Average', 'Good']}
	assert Vendor.compare_vendors(vendor1, vendor2) == (
		{'name': 'Vendor1', 'service_type': 'Catering', 'reviews': ['Good', 'Excellent']},
		{'name': 'Vendor2', 'service_type': 'Music', 'reviews': ['Average', 'Good']}
	)


def test_messaging_system():
	ms = MessagingSystem()
	ms.send_message('User1', 'Vendor1', 'Hello')
	ms.send_message('User2', 'Vendor1', 'Hi')
	assert ms.view_messages('Vendor1') == [
		{'from': 'User1', 'message': 'Hello'},
		{'from': 'User2', 'message': 'Hi'}
	]
