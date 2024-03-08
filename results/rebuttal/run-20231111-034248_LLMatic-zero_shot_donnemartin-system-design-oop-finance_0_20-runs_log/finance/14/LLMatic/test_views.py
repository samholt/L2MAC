from views import UserView
from models import User

def test_user_view():
	user_view = UserView()
	assert user_view.register('test', 'test', 'test@test.com') == 'User created successfully'
	assert user_view.login('test', 'test') == 'User authenticated'
	assert user_view.recover_password('test') == 'Password recovery link has been sent to your email'

# Rest of the tests remain the same


