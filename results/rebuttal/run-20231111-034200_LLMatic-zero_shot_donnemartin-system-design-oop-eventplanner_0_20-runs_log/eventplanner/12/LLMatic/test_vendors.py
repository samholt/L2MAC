import vendors

def test_vendor():
	vendor1 = vendors.Vendor('Vendor1', ['Service1', 'Service2'], ['Good', 'Excellent'])
	vendor2 = vendors.Vendor('Vendor2', ['Service1', 'Service2'], ['Good', 'Excellent'])
	vendors.vendors_db['Vendor1'] = vendor1
	vendors.vendors_db['Vendor2'] = vendor2

	assert vendor1.view_vendor() == {'name': 'Vendor1', 'services': ['Service1', 'Service2'], 'reviews': ['Good', 'Excellent']}
	assert vendor2.view_vendor() == {'name': 'Vendor2', 'services': ['Service1', 'Service2'], 'reviews': ['Good', 'Excellent']}
	assert vendor1.compare_vendors(vendor2) == True
	assert vendor1.send_message('Hello') == 'Message sent to Vendor1: Hello'

