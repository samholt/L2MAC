import vendors


def test_add_and_get_vendor():
	vendors.add_vendor(1, 'Vendor 1', ['Good', 'Excellent'])
	vendor = vendors.get_vendor(1)
	assert vendor is not None
	assert vendor.name == 'Vendor 1'
	assert vendor.reviews == ['Good', 'Excellent']


def test_get_all_vendors():
	vendors.add_vendor(2, 'Vendor 2', ['Average', 'Good'])
	all_vendors = vendors.get_all_vendors()
	assert len(all_vendors) == 2


def test_delete_vendor():
	vendors.delete_vendor(1)
	vendor = vendors.get_vendor(1)
	assert vendor is None


def test_update_vendor():
	vendors.update_vendor(2, name='Updated Vendor', reviews=['Excellent'])
	vendor = vendors.get_vendor(2)
	assert vendor.name == 'Updated Vendor'
	assert vendor.reviews == ['Excellent']
