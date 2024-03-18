from models.user import User

users = {}

def register_user(name, email, password):
	user = User(name, email, password)
	users[email] = user
	return user

def get_user(email):
	return users.get(email, None)

def update_user(email, **kwargs):
	user = users.get(email, None)
	if user:
		for key, value in kwargs.items():
			setattr(user, key, value)
	return user

def delete_user(email):
	users.pop(email, None)
