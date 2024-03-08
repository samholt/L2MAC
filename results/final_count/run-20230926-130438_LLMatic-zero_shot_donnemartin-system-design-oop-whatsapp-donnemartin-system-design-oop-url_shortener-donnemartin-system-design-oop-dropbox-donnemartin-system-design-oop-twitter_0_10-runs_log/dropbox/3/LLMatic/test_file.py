import file

def test_file_upload_download():
	file_db = file.FileDatabase()
	test_file = file.File('test', 'txt', 100, 'This is a test file')
	file_db.upload(test_file)
	downloaded_file = file_db.download('test')
	assert downloaded_file is not None
	assert downloaded_file.name == 'test'
	assert downloaded_file.type == 'txt'
	assert downloaded_file.size == 100
	assert downloaded_file.content == 'This is a test file'


def test_file_versioning():
	test_file = file.File('version_test', 'txt', 100, 'Version 1')
	test_file.add_version('Version 2')
	assert test_file.content == 'Version 2'
	test_file.restore_version(0)
	assert test_file.content == 'Version 1'


def test_folder_operations():
	folder = file.Folder('test_folder')
	file1 = file.File('file1', 'txt', 100, 'File 1')
	file2 = file.File('file2', 'txt', 100, 'File 2')
	folder.add_file(file1)
	folder.add_file(file2)
	assert 'file1' in folder.files
	assert 'file2' in folder.files
	folder.remove_file('file1')
	assert 'file1' not in folder.files
	folder2 = file.Folder('test_folder2')
	folder.move_file('file2', folder2)
	assert 'file2' not in folder.files
	assert 'file2' in folder2.files
	folder2.rename_file('file2', 'renamed_file')
	assert 'file2' not in folder2.files
	assert 'renamed_file' in folder2.files
