import re

# Mock database
users_db = {}

# User class
class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

# Function to validate email
def validate_email(email):
	if re.match(r"[^@]+@[^@]+\.[^@]+", email):
		return True
	return False

# Function to validate password
def validate_password(password):
	if len(password) >= 8 and any(char.isdigit() for char in password):
		return True
	return False

# Function to register a new user
def register_user(name, email, password):
	if validate_email(email) and validate_password(password):
		new_user = User(name, email, password)
		users_db[email] = new_user
		return True
	return False

# Function to authenticate a user
def authenticate_user(email, password):
	if email in users_db and users_db[email].password == password:
		return 'Login successful'
	return 'Login failed'
