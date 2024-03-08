from cloudsafe.app.models import User


class UserService:
	def __init__(self):
		self.users = {}

	def register_user(self, id, name, email, password, profile_picture):
		user = User(id, name, email, password, profile_picture)
		self.users[email] = user
		return 'User registered successfully'

	def login_user(self, email, password):
		user = self.users.get(email)
		if user and user.password == password:
			return 'Login successful'
		return 'Invalid email or password'

	def change_password(self, email, old_password, new_password):
		user = self.users.get(email)
		if user and user.password == old_password:
			user.password = new_password
			return 'Password changed successfully'
		return 'Invalid email or old password'

	def update_profile_picture(self, email, new_profile_picture):
		user = self.users.get(email)
		if user:
			user.profile_picture = new_profile_picture
			return 'Profile picture updated successfully'
		return 'User not found'
