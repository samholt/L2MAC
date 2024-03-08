import pytest
import file_sharing

def test_share():
	data = {'name': 'Test', 'shared_with': ['test@test.com']}
	response = file_sharing.share(data)
	assert response == {'message': 'File shared successfully'}


def test_shared_folders():
	data = {'name': 'Test'}
	response = file_sharing.shared_folders(data)
	assert 'name' in response
