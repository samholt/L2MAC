from models.permission import Permission
from controllers.permission_controller import PermissionController
from models.user import User
from models.file import File

def test_permission_creation():
	controller = PermissionController()
	user = User(1, 'Test User', 'test@example.com')
	file = File(1, 'Test File', 100, user)
	permission = controller.create_permission(1, user, file, 'read')
	assert isinstance(permission, Permission)
	assert permission.id == 1
	assert permission.user == user
	assert permission.file == file
	assert permission.permission_type == 'read'
