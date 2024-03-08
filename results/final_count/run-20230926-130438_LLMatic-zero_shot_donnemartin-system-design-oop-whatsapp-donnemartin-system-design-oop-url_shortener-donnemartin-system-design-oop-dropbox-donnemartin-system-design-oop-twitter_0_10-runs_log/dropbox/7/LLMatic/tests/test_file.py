from models.user import User
from models.file import File
from services.file_service import FileService


def test_upload_file():
	user = User(1, 'Test User', 'test@test.com', 'password', 'profile.jpg', 0)
	file_service = FileService()
	file = {'name': 'test.txt', 'type': 'txt', 'size': 500}
	assert file_service.upload_file(user, file) == 'File uploaded successfully'
	assert user.get_storage_used() == 500
	assert file_service.get_file(1).get_name() == 'test.txt'

	file = {'name': 'test.pdf', 'type': 'pdf', 'size': 1500}
	assert file_service.upload_file(user, file) == 'File size exceeds limit'

	file = {'name': 'test.exe', 'type': 'exe', 'size': 500}
	assert file_service.upload_file(user, file) == 'File type not allowed'


def test_download_file():
	user = User(1, 'Test User', 'test@test.com', 'password', 'profile.jpg', 0)
	file_service = FileService()
	file = {'name': 'test.txt', 'type': 'txt', 'size': 500}
	file_service.upload_file(user, file)
	assert file_service.download_file(1) == 'Download link: /download/1'
	assert file_service.download_file(2) == 'File not found'


def test_download_folder_as_zip():
	file_service = FileService()
	assert file_service.download_folder_as_zip('test_folder') == 'Download link: /download/Folder.zip'
