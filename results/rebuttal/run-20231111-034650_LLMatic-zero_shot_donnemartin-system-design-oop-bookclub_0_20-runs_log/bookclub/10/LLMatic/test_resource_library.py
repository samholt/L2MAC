import pytest
from resource_library import Resource, ResourceLibrary


def test_resource_library():
	library = ResourceLibrary()

	# Test adding a resource
	resource1 = Resource('1', 'Resource 1', 'This is resource 1', 'http://resource1.com')
	library.add_resource(resource1)
	assert library.get_resource('1') == resource1

	# Test updating a resource
	library.update_resource('1', title='Updated Resource 1', description='This is updated resource 1', link='http://updatedresource1.com')
	updated_resource1 = library.get_resource('1')
	assert updated_resource1.title == 'Updated Resource 1'
	assert updated_resource1.description == 'This is updated resource 1'
	assert updated_resource1.link == 'http://updatedresource1.com'

	# Test deleting a resource
	library.delete_resource('1')
	assert library.get_resource('1') is None
