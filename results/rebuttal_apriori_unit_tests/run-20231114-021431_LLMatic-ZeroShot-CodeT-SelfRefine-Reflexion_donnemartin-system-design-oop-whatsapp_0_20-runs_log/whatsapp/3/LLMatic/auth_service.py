users_db = {}

def sign_up(email, password):
	if email in users_db:
		return False
	users_db[email] = password
	return True

def recover_password(email):
	if email not in users_db:
		return False
	return users_db[email]
