import pytest
import file_sharing

def test_share():
	data = {'file_name': 'new_file.txt', 'shared_with': ['test2@test.com'], 'permissions': {'test2@test.com': 'read'}}
	response, status_code = file_sharing.share(data)
	assert status_code == 201
	assert response['message'] == 'File shared successfully'
