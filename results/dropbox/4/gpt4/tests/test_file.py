from models.file import File
from controllers.file_controller import FileController
from models.user import User

def test_file_creation():
	controller = FileController()
	user = User(1, 'Test User', 'test@example.com')
	file = controller.upload_file(1, 'Test File', 100, user)
	assert isinstance(file, File)
	assert file.id == 1
	assert file.name == 'Test File'
	assert file.size == 100
	assert file.owner == user
