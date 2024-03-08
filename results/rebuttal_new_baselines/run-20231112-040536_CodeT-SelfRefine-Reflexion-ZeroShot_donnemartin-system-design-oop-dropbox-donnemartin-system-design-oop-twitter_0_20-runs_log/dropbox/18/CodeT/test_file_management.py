import file_management

def test_upload():
	data = {'name': 'Test File', 'type': 'txt', 'size': 100, 'content': 'Hello, World!', 'versions': []}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'Test File'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert response['file']['name'] == 'Test File'

def test_organize():
	data = {'name': 'Test File', 'new_name': 'New Name'}
	response, status_code = file_management.organize(data)
	assert status_code == 200
	assert response['message'] == 'File organized successfully'

def test_get_version():
	response, status_code = file_management.get_version()
	assert status_code == 200
	assert len(response) == 1

def test_update_version():
	data = {'name': 'New Name', 'new_version': 'Hello, World! v2'}
	response, status_code = file_management.update_version(data)
	assert status_code == 200
	assert response['message'] == 'Version updated successfully'
