from resource import Resource

def test_resource():
	# Mock database
	db = {'resources': []}

	# Initialize Resource class
	resource = Resource(db)

	# Test add_resource
	resource.add_resource({'id': 1, 'title': 'Test Resource', 'content': 'This is a test resource.'})
	assert db['resources'] == [{'id': 1, 'title': 'Test Resource', 'content': 'This is a test resource.'}]

	# Test get_resources
	assert resource.get_resources() == [{'id': 1, 'title': 'Test Resource', 'content': 'This is a test resource.'}]

	# Test update_resource
	resource.update_resource(1, {'id': 1, 'title': 'Updated Test Resource', 'content': 'This is an updated test resource.'})
	assert db['resources'] == [{'id': 1, 'title': 'Updated Test Resource', 'content': 'This is an updated test resource.'}]

	# Test delete_resource
	resource.delete_resource(1)
	assert db['resources'] == []
