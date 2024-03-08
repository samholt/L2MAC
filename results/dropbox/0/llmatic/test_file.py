import pytest
from file import File

def test_file_upload():
	file = File(1, 'testfile', 100, 'content')
	file.upload('newcontent')
	assert file.file_content == 'newcontent'

def test_file_download():
	file = File(1, 'testfile', 100, 'content')
	assert file.download() == 'content'

def test_file_view():
	file = File(1, 'testfile', 100, 'content')
	assert file.view() == 'content'

def test_file_delete():
	file = File(1, 'testfile', 100, 'content')
	file.delete()
	assert file.file_content == None

