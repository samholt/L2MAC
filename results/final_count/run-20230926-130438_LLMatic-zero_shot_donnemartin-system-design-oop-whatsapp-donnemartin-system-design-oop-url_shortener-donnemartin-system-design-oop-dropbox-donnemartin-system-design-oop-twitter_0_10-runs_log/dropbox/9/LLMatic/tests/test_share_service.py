import pytest
from services.share_service import *
from models.file import File


def test_share_file():
	file = File('1', 'test content', 100, '2022-01-01', '1', [])
	files_db['1'] = file
	share_file('1', '1', '2')
	assert '2' in files_db['1'].shared_with


def test_activity_log():
	file = File('2', 'test content', 100, '2022-01-01', '1', [])
	files_db['2'] = file
	share_file('2', '1', '2')
	assert 'File with id 2 shared by user 1 with user 2' in get_activity_log()
