from users import UserManager

def test_user_management():
	user_manager = UserManager()

	# Test user creation
	assert user_manager.create_user(1, 'John Doe', 'john.doe@example.com') == 'User created successfully'
	assert user_manager.create_user(1, 'John Doe', 'john.doe@example.com') == 'User already exists'

	# Test user retrieval
	user = user_manager.get_user(1)
	assert user.id == 1
	assert user.name == 'John Doe'
	assert user.email == 'john.doe@example.com'

	# Test user update
	assert user_manager.update_user(1, name='Jane Doe', email='jane.doe@example.com') == 'User updated successfully'
	user = user_manager.get_user(1)
	assert user.name == 'Jane Doe'
	assert user.email == 'jane.doe@example.com'

	# Test user deletion
	assert user_manager.delete_user(1) == 'User deleted successfully'
	assert user_manager.get_user(1) is None

	# Test user following and unfollowing
	assert user_manager.create_user(2, 'Alice', 'alice@example.com') == 'User created successfully'
	user1 = user_manager.get_user(1)
	user2 = user_manager.get_user(2)
	if user1 and user2:
		user1.follow(user2)
		assert user2 in user1.following
		assert 'Jane Doe started following you.' in user2.get_feed()
		user1.unfollow(user2)
		assert user2 not in user1.following
		assert 'Jane Doe stopped following you.' in user2.get_feed()

	# Test user feed
	if user2:
		assert user_manager.get_user_feed(2) == user2.get_feed()
