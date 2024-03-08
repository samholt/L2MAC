from models.user import User

users_db = {}

def register_user(name, email, password, profile_picture):
	user = User(name, email, password, profile_picture, 0)
	users_db[email] = user
	return user

def login_user(email, password):
	user = users_db.get(email)
	if user and user.password == password:
		return user
	return None

def forgot_password(email, new_password):
	user = users_db.get(email)
	if user:
		user.password = new_password
		return True
	return False

def get_user_profile(email):
	return users_db.get(email)

def change_password(email, old_password, new_password):
	user = users_db.get(email)
	if user and user.password == old_password:
		user.password = new_password
		return True
	return False
