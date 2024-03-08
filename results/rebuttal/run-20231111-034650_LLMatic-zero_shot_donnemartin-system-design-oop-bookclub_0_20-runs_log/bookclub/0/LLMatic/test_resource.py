import pytest
from resource import Resource

def test_resource_creation():
	resource = Resource('Title', 'Content', 'Contributor')
	assert resource.title == 'Title'
	assert resource.content == 'Content'
	assert resource.contributor == 'Contributor'

def test_add_resource():
	resource = Resource('', '', '')
	resource.add_resource('New Title', 'New Content', 'New Contributor')
	assert resource.title == 'New Title'
	assert resource.content == 'New Content'
	assert resource.contributor == 'New Contributor'

def test_update_resource():
	resource = Resource('Title', 'Content', 'Contributor')
	resource.update_resource('Updated Title', 'Updated Content', 'Updated Contributor')
	assert resource.title == 'Updated Title'
	assert resource.content == 'Updated Content'
	assert resource.contributor == 'Updated Contributor'

def test_contribute():
	resource = Resource('Title', 'Content', 'Contributor')
	resource.contribute(' Additional Content')
	assert resource.content == 'Content Additional Content'
