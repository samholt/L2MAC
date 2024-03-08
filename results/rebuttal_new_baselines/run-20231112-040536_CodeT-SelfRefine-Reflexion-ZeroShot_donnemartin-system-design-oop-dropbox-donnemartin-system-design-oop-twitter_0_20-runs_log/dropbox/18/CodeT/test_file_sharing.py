import file_sharing

def test_share():
	data = {'file_name': 'New Name', 'shared_with': ['user2@example.com'], 'permissions': {'user2@example.com': 'read'}}
	response, status_code = file_sharing.share(data)
	assert status_code == 201
	assert response['message'] == 'File shared successfully'
