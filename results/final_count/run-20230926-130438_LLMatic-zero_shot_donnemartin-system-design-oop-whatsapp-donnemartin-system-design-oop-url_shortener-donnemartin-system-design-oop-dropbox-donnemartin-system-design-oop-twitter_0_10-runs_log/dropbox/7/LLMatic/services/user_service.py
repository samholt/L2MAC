from models.user import User
import random
import string

# Mock database
users_db = {}

def register_user(name, email, password):
	# Check if email is already in use
	if email in users_db:
		return 'Email already in use'
	
	# Create new User object
	user = User(None, name, email, password, None, 0)
	
	# Add user to database
	users_db[email] = user
	
	return 'User registered successfully'

def login_user(email, password):
	# Check if user exists
	if email not in users_db or users_db[email].get_password() != password:
		return 'Invalid email or password'
	
	# Return user
	return users_db[email]

def forgot_password(email):
	# Check if user exists
	if email not in users_db:
		return 'Email not found'
	
	# Generate temporary password
	temp_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
	
	# Set user's password to temporary password
	users_db[email].set_password(temp_password)
	
	# Send temporary password to user's email
	# In a real application, we would use an email service here
	print(f'Sent temporary password to {email}')
	
	return temp_password

def get_profile(email):
	# Check if user exists
	if email not in users_db:
		return 'User not found'
	
	# Return user's profile
	user = users_db[email]
	return {
		'name': user.get_name(),
		'email': user.get_email(),
		'profile_picture': user.get_profile_picture(),
		'storage_used': user.get_storage_used()
	}

def change_password(email, new_password):
	# Check if user exists
	if email not in users_db:
		return 'User not found'
	
	# Change user's password
	users_db[email].set_password(new_password)
	return 'Password changed successfully'

def log_activity(email, action):
	# Check if user exists
	if email not in users_db:
		return 'User not found'
	
	# Add action to user's activity log
	users_db[email].add_to_activity_log(action)
	
	# Return updated activity log
	return users_db[email].get_activity_log()
