import pytest
from cloudsafe.app.file_service import FileService


def test_file_service():
	file_service = FileService()

	# Test file upload
	assert file_service.upload_file(1, 'file1', 1) == 'File uploaded successfully'
	assert file_service.upload_file(2, 'file2', 1, 1) == 'File uploaded successfully'

	# Test file download
	assert file_service.download_file(1) == 'File downloaded successfully'
	assert file_service.download_file(3) == 'File not found'

	# Test file move
	assert file_service.move_file(1, 2) == 'File moved successfully'
	assert file_service.move_file(3, 2) == 'File not found'

	# Test file rename
	assert file_service.rename_file(1, 'new_file1') == 'File renamed successfully'
	assert file_service.rename_file(3, 'new_file3') == 'File not found'

	# Test file delete
	assert file_service.delete_file(1) == 'File deleted successfully'
	assert file_service.delete_file(3) == 'File not found'

	# Test folder create
	assert file_service.create_folder(1, 'folder1', 1) == 'Folder created successfully'
	assert file_service.create_folder(2, 'folder2', 1, 1) == 'Folder created successfully'

	# Test folder rename
	assert file_service.rename_folder(1, 'new_folder1') == 'Folder renamed successfully'
	assert file_service.rename_folder(3, 'new_folder3') == 'Folder not found'

	# Test folder move
	assert file_service.move_folder(1, 2) == 'Folder moved successfully'
	assert file_service.move_folder(3, 2) == 'Folder not found'

	# Test folder delete
	assert file_service.delete_folder(1) == 'Folder deleted successfully'
	assert file_service.delete_folder(3) == 'Folder not found'

