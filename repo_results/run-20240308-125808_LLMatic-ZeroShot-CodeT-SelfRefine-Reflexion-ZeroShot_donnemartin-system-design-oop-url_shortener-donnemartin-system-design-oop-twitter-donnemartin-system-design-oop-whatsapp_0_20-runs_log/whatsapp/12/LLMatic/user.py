class User:
	def __init__(self, email, password, profile_picture=None, status_message=None, privacy='public'):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy = privacy

mock_db = {}

def sign_up(email, password, profile_picture=None, status_message=None, privacy='public'):
	if email in mock_db:
		return 'User already exists'
	else:
		mock_db[email] = User(email, password, profile_picture, status_message, privacy)
		return 'User created successfully'

def recover_password(email):
	if email in mock_db:
		new_password = 'new_password'
		mock_db[email].password = new_password
		return 'Password reset successful'
	else:
		return 'User does not exist'
