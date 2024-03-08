from controller import Controller
from view import View
from file import File

def test_view():
	controller = Controller('test_db')
	view = View(controller)
	
	# Test create_user
	user = view.create_user('test_user', 'password')
	assert user.username == 'test_user'
	assert user.password == 'password'
	
	# Test upload_file
	file = view.upload_file('test_user', 'test_file', 100, 'file_content')
	assert file.name == 'test_file'
	assert file.size == 100
	assert file.content == 'file_content'
	
	# Test view_file
	file_view = view.view_file('test_user', file.id)
	assert file_view == 'file_content'
	
	# Test search_file
	file_id = view.search_file('test_user', 'test_file')
	assert file_id == file.id
	
	# Test share_file
	user2 = view.create_user('test2', 'password')
	assert view.share_file('test_user', file.id, 'test2', 'r')
	
	# Test download_file
	file_download = view.download_file('test2', file.id)
	assert file_download == 'file_content'
