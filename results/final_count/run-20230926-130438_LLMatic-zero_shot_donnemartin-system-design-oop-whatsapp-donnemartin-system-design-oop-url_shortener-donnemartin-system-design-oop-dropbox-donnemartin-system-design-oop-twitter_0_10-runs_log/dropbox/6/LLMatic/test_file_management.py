import pytest
from file_management.routes import files_db, folders_db
from file_management.models import File, Folder


def test_file_folder_management():
	# Test file upload
	files_db['test.txt'] = File('test.txt', 'text/plain', 4, b'test', 1)
	assert 'test.txt' in files_db

	# Test file rename
	files_db['test.txt'].name = 'new.txt'
	files_db['new.txt'] = files_db.pop('test.txt')
	assert 'new.txt' in files_db

	# Test folder creation
	folders_db['test'] = Folder('test', {})
	assert 'test' in folders_db

	# Test file move
	folders_db['test'].files['new.txt'] = files_db.pop('new.txt')
	assert 'new.txt' in folders_db['test'].files

	# Test file delete
	files_db.pop('new.txt', None)
	assert 'new.txt' not in files_db

	# Test file restore
	files_db['test.txt'] = File('test.txt', 'text/plain', 4, b'test', 1)
	files_db['test.txt'].version = 1
	assert files_db['test.txt'].version == 1

