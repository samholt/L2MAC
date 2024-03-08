from users import UserManager
from database import MockDatabase

def test_user_management():
	db = MockDatabase()
	user_manager = UserManager(db)

	# Test user creation
	user1 = user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	assert user1.id == 1
	assert user1.name == 'John Doe'
	assert user1.email == 'john.doe@example.com'
	assert user_manager.create_user(1, 'John Doe', 'john.doe@example.com') == 'User already exists'

	# Test user retrieval
	user = user_manager.get_user(1)
	assert user.id == 1
	assert user.name == 'John Doe'
	assert user.email == 'john.doe@example.com'

	# Test user deletion
	assert user_manager.delete_user(1) == 'User deleted successfully'
	assert user_manager.get_user(1) == 'User not found'

	# Test user following
	user1 = user_manager.create_user(2, 'Alice', 'alice@example.com')
	user2 = user_manager.create_user(3, 'Bob', 'bob@example.com')
	user1.follow(user2)
	assert user2.id in user1.following

	# Test user unfollowing
	user1.unfollow(user2)
	assert user2.id not in user1.following
