from services.user_service import UserService

def test_user_service():
	user_service = UserService()

	# Test registration
	assert user_service.register('test@test.com', 'password')
	assert not user_service.register('test@test.com', 'password')

	# Test authentication
	assert user_service.authenticate('test@test.com', 'password')
	assert not user_service.authenticate('test@test.com', 'wrong_password')

	# Test profile management
	assert user_service.set_profile('test@test.com', 'picture.jpg', 'Hello, world!')
	assert not user_service.set_profile('nonexistent@test.com', 'picture.jpg', 'Hello, world!')

	# Test privacy settings
	assert user_service.set_privacy('test@test.com', True)
	assert not user_service.set_privacy('nonexistent@test.com', True)

	# Test contact management
	assert user_service.register('contact@test.com', 'password')
	assert user_service.block_contact('test@test.com', 'contact@test.com')
	assert not user_service.block_contact('test@test.com', 'contact@test.com')
	assert user_service.unblock_contact('test@test.com', 'contact@test.com')
	assert not user_service.unblock_contact('test@test.com', 'contact@test.com')
	assert not user_service.block_contact('test@test.com', 'nonexistent@test.com')
	assert not user_service.unblock_contact('test@test.com', 'nonexistent@test.com')
