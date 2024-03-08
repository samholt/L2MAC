import hashlib
from models.user import User

class UserService:
	# Mock database
	users_db = {}

	@staticmethod
	def register_user(name, email, password):
		if email in UserService.users_db:
			return 'Email already exists'
		hashed_password = hashlib.sha256(password.encode()).hexdigest()
		user = User(None, name, email, hashed_password, None, 0)
		UserService.users_db[email] = user
		return 'User registered successfully'

	@staticmethod
	def login_user(email, password):
		if email not in UserService.users_db:
			return 'User does not exist'
		user = UserService.users_db[email]
		if not user.check_password(password):
			return 'Incorrect password'
		return 'User logged in successfully'

	@staticmethod
	def reset_password(email, new_password):
		if email not in UserService.users_db:
			return 'User does not exist'
		hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
		UserService.users_db[email].password = hashed_password
		return 'Password reset successfully'
