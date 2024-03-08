from controller import Controller
from file import File

def test_controller():
	controller = Controller('test.db')
	
	# Test user creation
	user = controller.create_user('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'
	
	# Test file upload
	file = controller.upload_file('test', 'file1', 100, 'content')
	assert file.name == 'file1'
	assert file.size == 100
	assert file.content == 'content'
	
	# Test file view
	content = controller.view_file('test', file.id)
	assert content == 'content'
	
	# Test file search
	file_id = controller.search_file('test', 'file1')
	assert file_id == file.id
	
	# Test file share
	user2 = controller.create_user('test2', 'password')
	assert controller.share_file('test', file.id, 'test2', 'r')
	
	# Test file download
	content = controller.download_file('test2', file.id)
	assert content == 'content'
