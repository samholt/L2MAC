from cloudsafe.app.models import User, File, Folder

def test_user_model():
	user = User(1, 'Test User', 'test@example.com', 'password', 'profile.jpg', 0)
	assert user.id == 1
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.profile_picture == 'profile.jpg'
	assert user.storage_used == 0
	assert 'pbkdf2:sha256' in user.password

def test_file_model():
	file = File(1, 'Test File', 100, 'txt', '/path/to/file', 1)
	assert file.id == 1
	assert file.name == 'Test File'
	assert file.size == 100
	assert file.type == 'txt'
	assert file.path == '/path/to/file'
	assert file.user_id == 1

def test_folder_model():
	folder = Folder(1, 'Test Folder', 1)
	assert folder.id == 1
	assert folder.name == 'Test Folder'
	assert folder.user_id == 1
