import pytest
import file_sharing

def test_share():
	data = {'file_name': 'new_file.txt', 'expiry_date': '2022-12-31', 'password': 'share'}
	response, status_code = file_sharing.share(data)
	assert status_code == 201
	assert response['message'] == 'File shared successfully'
