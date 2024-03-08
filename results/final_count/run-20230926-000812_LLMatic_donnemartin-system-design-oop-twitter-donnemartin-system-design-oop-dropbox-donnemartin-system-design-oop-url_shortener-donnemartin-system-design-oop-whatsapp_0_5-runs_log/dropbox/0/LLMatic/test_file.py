import pytest
from file import File, Folder, upload, download
from user import register

def test_file_upload_download():
	register('Test User', 'test@example.com', 'password')
	file = File('test.txt', 'text', 10, 'This is a test file')
	assert upload(file, 'test@example.com') == 'File uploaded successfully'
	downloaded_file = download('test.txt', 'test@example.com')
	assert downloaded_file == 'This is a test file'

def test_file_folder_organization():
	folder = Folder('Test Folder')
	file = File('test.txt', 'text', 10, 'This is a test file')
	folder.add_file(file)
	assert folder.files[0].name == 'test.txt'
	folder.rename('New Folder')
	assert folder.name == 'New Folder'
	file.rename('new.txt')
	assert file.name == 'new.txt'
	folder2 = Folder('Folder 2')
	file.move(folder2)
	assert file.folder == folder2
	folder.add_folder(folder2)
	assert folder.delete_file('new.txt') == 'File deleted successfully'
	assert folder.delete_folder('Folder 2') == 'Folder deleted successfully'

def test_file_versioning():
	register('Test User 2', 'test2@example.com', 'password')
	file = File('test.txt', 'text', 10, 'This is a test file')
	assert upload(file, 'test2@example.com') == 'File uploaded successfully'
	file2 = File('test.txt', 'text', 10, 'This is a new version of the test file')
	assert upload(file2, 'test2@example.com') == 'File version uploaded successfully'
	downloaded_file = download('test.txt', 'test2@example.com', 1)
	assert downloaded_file == 'This is a new version of the test file'
