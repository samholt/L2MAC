import pytest
from resource_library import ResourceLibrary

def test_share_resource():
	resource_library = ResourceLibrary()
	assert resource_library.share_resource('user1', 'resource1') == 'Resource shared successfully'
	assert resource_library.library['user1'] == ['resource1']

def test_contribute_to_library():
	resource_library = ResourceLibrary()
	assert resource_library.contribute_to_library('user1', 'resource1') == 'Resource contributed successfully'
	assert resource_library.library['contributions'] == [{'user1': 'resource1'}]
