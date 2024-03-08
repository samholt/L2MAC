import pytest
from services.file_service import *
from models.file import File


def test_upload_file():
	file = File('1', 'test content', 100, '2022-01-01', '1', [])
	upload_file(file)
	assert '1' in files_db
	assert files_db['1'].content != 'test content'


def test_download_file():
	file = File('2', 'test content', 100, '2022-01-01', '1', [])
	upload_file(file)
	content = download_file('2', '1')
	assert content == 'test content'


def test_delete_file():
	file = File('3', 'test content', 100, '2022-01-01', '1', [])
	upload_file(file)
	delete_file('3', '1')
	assert '3' not in files_db


def test_share_file():
	file = File('4', 'test content', 100, '2022-01-01', '1', [])
	upload_file(file)
	share_file('4', '1', '2')
	assert '2' in files_db['4'].shared_with


def test_activity_log():
	file = File('5', 'test content', 100, '2022-01-01', '1', [])
	upload_file(file)
	assert 'File with id 5 uploaded by user 1' in get_activity_log()
	content = download_file('5', '1')
	assert 'File with id 5 downloaded by user 1' in get_activity_log()
	share_file('5', '1', '2')
	assert 'File with id 5 shared by user 1 with user 2' in get_activity_log()
	delete_file('5', '1')
	assert 'File with id 5 deleted by user 1' in get_activity_log()
