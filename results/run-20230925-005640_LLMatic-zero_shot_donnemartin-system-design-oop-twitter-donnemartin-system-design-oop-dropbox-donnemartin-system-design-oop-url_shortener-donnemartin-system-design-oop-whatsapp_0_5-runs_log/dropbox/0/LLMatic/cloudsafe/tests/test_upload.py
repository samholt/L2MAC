import pytest
import requests
import os
from unittest.mock import patch, MagicMock

@pytest.fixture
def file_to_upload():
	with open('test_file.txt', 'w') as f:
		f.write('This is a test file.')
	return open('test_file.txt', 'r')

def test_upload(file_to_upload):
	url = 'http://localhost:5000/upload'
	data = {
		'name': 'test_file.txt',
		'size': os.path.getsize('test_file.txt'),
		'type': 'text/plain',
		'user_id': 1
	}
	files = {'file': file_to_upload}
	mock_response = MagicMock()
	mock_response.status_code = 201
	mock_response.json.return_value = {'file_id': 1}
	with patch('requests.post', return_value=mock_response) as mock_post:
		response = requests.post(url, files=files, data=data)
		mock_post.assert_called_once_with(url, files=files, data=data)
	assert response.status_code == 201
	assert 'file_id' in response.json()
	file_to_upload.close()
	os.remove('test_file.txt')
