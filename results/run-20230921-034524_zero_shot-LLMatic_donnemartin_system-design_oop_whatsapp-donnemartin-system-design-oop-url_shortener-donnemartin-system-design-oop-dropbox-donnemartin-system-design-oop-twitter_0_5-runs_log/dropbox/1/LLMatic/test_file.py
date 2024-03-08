import pytest
from file import File

def test_file_upload():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	file.upload()
	assert file.file_name == 'test_file'
	assert file.file_size == 1024
	assert file.file_type == 'txt'
	assert file.file_content == 'This is a test file'

def test_file_download():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	file.download()
	# Add assertions for download

def test_file_view():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	file.view()
	# Add assertions for view

def test_file_delete():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	file.delete()
	# Add assertions for delete

def test_get_metadata():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	metadata = file.get_metadata()
	assert metadata['file_name'] == 'test_file'
	assert metadata['file_size'] == 1024
	assert metadata['file_type'] == 'txt'
