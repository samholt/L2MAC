from models.user import User
from controllers.user_controller import UserController

def test_user_creation():
	controller = UserController()
	user = controller.create_user(1, 'Test User', 'test@example.com')
	assert isinstance(user, User)
	assert user.id == 1
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
