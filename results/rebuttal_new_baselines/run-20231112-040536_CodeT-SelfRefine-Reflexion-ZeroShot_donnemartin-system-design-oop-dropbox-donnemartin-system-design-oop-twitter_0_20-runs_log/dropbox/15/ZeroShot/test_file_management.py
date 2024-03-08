import file_management

def test_upload():
	data = {'name': 'test.txt', 'type': 'text', 'size': 10, 'content': 'Test content', 'versions': []}
	response = file_management.upload(data)
	assert response['status'] == 'success'

def test_download():
	data = {'name': 'test.txt'}
	response = file_management.download(data)
	assert 'content' in response

def test_organize():
	data = {'old_name': 'test.txt', 'new_name': 'new_test.txt'}
	response = file_management.organize(data)
	assert response['status'] == 'success'

def test_get_versions():
	data = {'name': 'new_test.txt'}
	response = file_management.get_versions(data)
	assert 'versions' in response

def test_restore_version():
	data = {'name': 'new_test.txt', 'version': 'Test content'}
	response = file_management.restore_version(data)
	assert response['status'] == 'success'
