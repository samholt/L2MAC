import pytest
from cloudsafe.models.user import User


def test_register():
	User.register('Test User', 'test@example.com', 'password', 'https://example.com/profile.jpg')

	# Connect to the database
	conn = sqlite3.connect('cloudsafe.db')
	c = conn.cursor()

	# Retrieve the user with the given email
	c.execute("""SELECT * FROM users WHERE email = ?""", ('test@example.com',))
	user = c.fetchone()

	# Assert that the user was successfully registered
	assert user is not None


def test_authenticate():
	# Register a test user
	User.register('Test User', 'test@example.com', 'password', 'https://example.com/profile.jpg')

	# Authenticate the test user
	user = User.authenticate('test@example.com', 'password')

	# Assert that the user was successfully authenticated
	assert user is not None


def test_update_profile():
	# Register a test user
	User.register('Test User', 'test@example.com', 'password', 'https://example.com/profile.jpg')

	# Authenticate the test user
	user = User.authenticate('test@example.com', 'password')

	# Update the test user's profile
	user.update_profile('Updated User', 'updated@example.com', 'newpassword', 'https://example.com/newprofile.jpg')

	# Authenticate the updated user
	updated_user = User.authenticate('updated@example.com', 'newpassword')

	# Assert that the user's profile was successfully updated
	assert updated_user is not None


def test_calculate_storage_used():
	# Register a test user
	User.register('Test User', 'test@example.com', 'password', 'https://example.com/profile.jpg')

	# Authenticate the test user
	user = User.authenticate('test@example.com', 'password')

	# Calculate the test user's storage used
	user.calculate_storage_used()

	# Assert that the user's storage used was successfully calculated
	assert user.storage_used == 0
