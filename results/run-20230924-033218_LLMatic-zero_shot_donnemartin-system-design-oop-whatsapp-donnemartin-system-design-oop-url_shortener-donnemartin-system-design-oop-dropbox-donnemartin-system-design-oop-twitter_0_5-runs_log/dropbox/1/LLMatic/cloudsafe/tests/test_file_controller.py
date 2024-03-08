import pytest
from cloudsafe.app import create_app
from cloudsafe.app.file_service import FileService

@pytest.fixture

def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client


def test_upload_file(client):
	response = client.post('/upload', json={'id': '1', 'name': 'file1', 'user_id': 'user1', 'folder_id': 'folder1'})
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download_file(client):
	response = client.get('/download/1')
	assert response.get_json() == {'message': 'File downloaded successfully'}


def test_move_file(client):
	response = client.put('/move/1', json={'new_folder_id': 'folder2'})
	assert response.get_json() == {'message': 'File moved successfully'}


def test_rename_file(client):
	response = client.put('/rename/1', json={'new_name': 'file2'})
	assert response.get_json() == {'message': 'File renamed successfully'}


def test_delete_file(client):
	response = client.delete('/delete/1')
	assert response.get_json() == {'message': 'File deleted successfully'}


def test_create_folder(client):
	response = client.post('/folder/create', json={'id': '1', 'name': 'folder1', 'user_id': 'user1', 'parent_folder_id': None})
	assert response.get_json() == {'message': 'Folder created successfully'}


def test_rename_folder(client):
	response = client.put('/folder/rename/1', json={'new_name': 'folder2'})
	assert response.get_json() == {'message': 'Folder renamed successfully'}


def test_move_folder(client):
	response = client.put('/folder/move/1', json={'new_parent_folder_id': 'folder2'})
	assert response.get_json() == {'message': 'Folder moved successfully'}


def test_delete_folder(client):
	response = client.delete('/folder/delete/1')
	assert response.get_json() == {'message': 'Folder deleted successfully'}
