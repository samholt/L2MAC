import pytest
from resource import Resource

def test_resource():
	resource = Resource()
	resource.add_resource('Test Title', 'Test Content')
	assert resource.view_resources() == {'Test Title': 'Test Content'}
