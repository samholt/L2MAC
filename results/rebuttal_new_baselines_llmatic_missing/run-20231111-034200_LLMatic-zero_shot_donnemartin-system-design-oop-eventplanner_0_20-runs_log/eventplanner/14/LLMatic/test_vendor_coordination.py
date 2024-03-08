import pytest
from vendor_coordination import Vendor

def test_vendor():
	vendor1 = Vendor('Vendor1', ['service1', 'service2'], ['review1', 'review2'])
	vendor2 = Vendor('Vendor2', ['service3', 'service4'], ['review3', 'review4'])

	assert vendor1.view_profile() == {'name': 'Vendor1', 'services': ['service1', 'service2'], 'reviews': ['review1', 'review2']}
	assert vendor2.view_profile() == {'name': 'Vendor2', 'services': ['service3', 'service4'], 'reviews': ['review3', 'review4']}

	assert vendor1.compare_to(vendor2) == ({'name': 'Vendor1', 'services': ['service1', 'service2'], 'reviews': ['review1', 'review2']}, {'name': 'Vendor2', 'services': ['service3', 'service4'], 'reviews': ['review3', 'review4']})

	vendor1.send_message('Hello Vendor1')
	assert vendor1.messages == ['Hello Vendor1']

	vendor2.send_message('Hello Vendor2')
	assert vendor2.messages == ['Hello Vendor2']
