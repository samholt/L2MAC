import requests
import json


def test_share_link():
	data = {
		'file_id': 1,
		'expiry_date': '2022-12-31',
		'password': 'password'
	}
	response = requests.post('http://localhost:5000/share-link', json=data)
	assert response.status_code == 200
	assert 'share_link' in response.json()


def test_share_folder():
	data = {
		'folder_id': 1,
		'user_email': 'test@example.com',
		'permissions': 'read'
	}
	response = requests.post('http://localhost:5000/share-folder', json=data)
	assert response.status_code == 200
	assert response.json()['message'] == 'Folder shared successfully'

