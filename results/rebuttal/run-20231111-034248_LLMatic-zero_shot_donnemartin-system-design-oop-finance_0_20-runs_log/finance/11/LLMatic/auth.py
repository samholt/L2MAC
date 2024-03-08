import hashlib
from models import User


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password, email):
	if User.exists(username):
		return False
	User.create(username, hash_password(password), email)
	return True


def login_user(username, password):
	user = User.get(username)
	if user and user.password == hash_password(password):
		return True
	return False


def logout_user(username):
	# In a real application, this would involve removing the user's session or token
	# But for this mock application, we'll just return True
	return True
