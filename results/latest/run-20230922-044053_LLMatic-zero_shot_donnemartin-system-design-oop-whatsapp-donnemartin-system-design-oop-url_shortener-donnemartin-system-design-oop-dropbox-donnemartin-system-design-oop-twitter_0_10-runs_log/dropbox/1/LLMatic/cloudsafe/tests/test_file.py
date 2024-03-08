import pytest
from cloudsafe.file.models import File
from cloudsafe.file.views import upload, download, organize, versioning


def test_upload():
	response = upload()
	assert response.status_code == 200
	assert 'message' in response.json
	assert response.json['message'] == 'File uploaded successfully'


def test_download():
	file = File(name='test', size=1, type='text/plain', upload_date=None, version=1, parent_folder=None)
	response = download(file.id)
	assert response.status_code == 200


def test_organize():
	file = File(name='test', size=1, type='text/plain', upload_date=None, version=1, parent_folder=None)
	response = organize(file.id)
	assert response.status_code == 200
	assert 'message' in response.json
	assert response.json['message'] == 'File organized successfully'


def test_versioning():
	file = File(name='test', size=1, type='text/plain', upload_date=None, version=1, parent_folder=None)
	response = versioning(file.id)
	assert response.status_code == 200
	assert 'message' in response.json
	assert response.json['message'] == 'File version updated successfully'
