import vendor_coordination


def test_vendor_class():
	vendor = vendor_coordination.Vendor('Test Vendor', ['service1', 'service2'], [], [])
	assert vendor.name == 'Test Vendor'
	assert vendor.services == ['service1', 'service2']
	assert vendor.reviews == []
	assert vendor.messages == []


def test_view_vendor_profile():
	vendor = vendor_coordination.Vendor('Test Vendor', ['service1', 'service2'], [], [])
	profile = vendor_coordination.view_vendor_profile(vendor)
	assert profile == {'name': 'Test Vendor', 'services': ['service1', 'service2'], 'reviews': [], 'messages': []}


def test_compare_vendors():
	vendor1 = vendor_coordination.Vendor('Vendor1', ['service1', 'service2'], [], [])
	vendor2 = vendor_coordination.Vendor('Vendor2', ['service1', 'service2'], [], [])
	assert vendor_coordination.compare_vendors(vendor1, vendor2) == True


def test_communicate_with_vendor():
	vendor = vendor_coordination.Vendor('Test Vendor', ['service1', 'service2'], [], [])
	vendor_coordination.communicate_with_vendor(vendor, 'Test message')
	assert vendor.messages == ['Test message']

