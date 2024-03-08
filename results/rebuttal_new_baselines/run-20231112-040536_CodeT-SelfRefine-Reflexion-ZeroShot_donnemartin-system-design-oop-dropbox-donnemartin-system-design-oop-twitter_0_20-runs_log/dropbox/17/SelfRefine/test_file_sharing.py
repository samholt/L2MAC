import pytest
import file_sharing

def test_share_file():
	data = {'name': 'New Test File', 'shared_with': 'test2@example.com'}
	response = file_sharing.share_file(data)
	assert response['status'] == 'success'
	assert response['message'] == 'File shared successfully'

def test_shared_folders():
	data = {'name': 'New Test File'}
	response = file_sharing.shared_folders(data)
	assert response['status'] == 'success'
	assert response['data']['name'] == 'New Test File'
	assert response['data']['shared_with'] == 'test2@example.com'
