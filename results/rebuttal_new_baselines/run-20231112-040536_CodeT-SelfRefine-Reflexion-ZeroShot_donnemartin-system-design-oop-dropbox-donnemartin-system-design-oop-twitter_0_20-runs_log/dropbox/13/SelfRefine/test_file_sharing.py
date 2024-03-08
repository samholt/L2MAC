import pytest
import file_sharing

def test_share_link():
	data = {'file_name': 'new_test.txt', 'shared_with': [], 'permissions': {'view': True}}
	response = file_sharing.share_link(data)
	assert response == {'message': 'Link shared successfully'}

def test_shared_folder():
	data = {'file_name': 'new_test.txt', 'email': 'test@test.com'}
	response = file_sharing.shared_folder(data)
	assert response == {'message': 'Folder shared successfully'}
