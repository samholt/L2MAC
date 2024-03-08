import pytest
import file_sharing

def test_share_file():
	data = {'name': 'Test', 'url': 'http://test.com', 'expiry_date': '2022-12-31', 'password': 'test'}
	response = file_sharing.share_file(data)
	assert response == {'message': 'File shared successfully'}

def test_shared_folder():
	data = {}
	response = file_sharing.shared_folder(data)
	assert response == {'message': 'Folder shared successfully'}
