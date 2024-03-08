class User:
	def __init__(self, name, email, password, profile_picture='default.jpg', storage_used=0, storage_remaining=100):
		self.name = name
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.storage_used = storage_used
		self.storage_remaining = storage_remaining

mock_db = {}

def register(name, email, password):
	user = User(name, email, password)
	mock_db[email] = user
	return user

def login(email, password):
	if email in mock_db and mock_db[email].password == password:
		return True
	return False

def forgot_password(email, new_password):
	if email in mock_db:
		mock_db[email].password = new_password
		return True
	return False

def profile(email):
	if email in mock_db:
		user = mock_db[email]
		return {'name': user.name, 'email': user.email, 'profile_picture': user.profile_picture, 'storage_used': user.storage_used, 'storage_remaining': user.storage_remaining}
	return None

def change_password(email, new_password):
	if email in mock_db:
		mock_db[email].password = new_password
		return True
	return False
