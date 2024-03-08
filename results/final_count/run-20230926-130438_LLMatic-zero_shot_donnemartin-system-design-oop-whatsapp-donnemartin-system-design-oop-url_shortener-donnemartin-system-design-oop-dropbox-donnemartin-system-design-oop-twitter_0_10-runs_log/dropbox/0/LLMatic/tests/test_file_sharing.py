import pytest
from services.file_service import FileService

file_service = FileService()


def test_generate_shareable_link():
	file = {'name': 'test.txt', 'type': 'text', 'size': 1, 'path': '/'}
	user = 'test_user'
	uploaded_file = file_service.upload_file(file, user)
	file_id = uploaded_file['id']
	link = file_service.generate_shareable_link(file_id)
	assert link == 'http://localhost:5000/download/' + str(file_id)

	# Test for non-existent file
	assert file_service.generate_shareable_link(999) == 'File not found'
