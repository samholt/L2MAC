from services.file_service import FileService


def test_share_folder():
	file_service = FileService()
	file_service.create_folder('test_folder')
	file_service.share_folder('test_folder', 'test@example.com', 'read')
	assert ('test@example.com', 'read') in file_service.shared_folders['test_folder']
