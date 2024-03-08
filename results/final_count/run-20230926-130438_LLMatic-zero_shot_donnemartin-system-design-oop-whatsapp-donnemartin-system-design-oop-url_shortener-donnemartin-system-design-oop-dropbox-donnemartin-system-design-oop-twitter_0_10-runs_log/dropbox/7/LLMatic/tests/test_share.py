from services.share_service import ShareService


def test_share_file():
	share_service = ShareService()
	share_service.share_file('file1', 'user1')
	shared_files = share_service.get_shared_files()
	assert 'file1' in shared_files
	assert shared_files['file1'] == 'user1'


def test_share_folder():
	share_service = ShareService()
	share_service.share_folder('folder1', 'user1', 'read')
	shared_folders = share_service.get_shared_folders()
	assert 'folder1' in shared_folders
	assert shared_folders['folder1']['user_id'] == 'user1'
	assert shared_folders['folder1']['permissions'] == 'read'
