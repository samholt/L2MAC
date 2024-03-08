import vendor_coordination

vendor1 = vendor_coordination.Vendor('Vendor1', 'Profile1', ['Good', 'Excellent'])
vendor2 = vendor_coordination.Vendor('Vendor2', 'Profile2', ['Bad', 'Poor'])


def test_view_profile():
	assert vendor1.view_profile() == 'Profile1'


def test_compare_profiles():
	assert not vendor1.compare_profiles(vendor2)


def test_view_reviews():
	assert 'Good' in vendor1.view_reviews()


def test_send_message():
	assert vendor1.send_message('Hello')

