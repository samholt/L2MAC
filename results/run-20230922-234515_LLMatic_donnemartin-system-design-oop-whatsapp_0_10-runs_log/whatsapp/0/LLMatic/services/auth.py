import sqlite3
from models.user import User
from utils.hashing import hash_password, generate_password_reset_token

def create_users_table():
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT, profile_picture TEXT, status_message TEXT, last_seen_status TEXT, privacy_settings TEXT)')

def register_user(email: str, password: str) -> User:
	create_users_table()
	hashed_password = hash_password(password)
	user = User(id=None, email=email, password=hashed_password, profile_picture='', status_message='', last_seen_status='', privacy_settings={})
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('INSERT INTO users (email, password, profile_picture, status_message, last_seen_status, privacy_settings) VALUES (?, ?, ?, ?, ?, ?)', (user.email, user.password, user.profile_picture, user.status_message, user.last_seen_status, str(user.privacy_settings)))
		user.id = cursor.lastrowid
	return user

def get_user(user_id: int) -> User:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
		user_data = cursor.fetchone()
		return User(id=user_data[0], email=user_data[1], password=user_data[2], profile_picture=user_data[3], status_message=user_data[4], last_seen_status=user_data[5], privacy_settings=eval(user_data[6]))

def set_profile_picture(user_id: int, new_picture: str) -> User:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('UPDATE users SET profile_picture = ? WHERE id = ?', (new_picture, user_id))
	return get_user(user_id)

def set_status_message(user_id: int, new_message: str) -> User:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('UPDATE users SET status_message = ? WHERE id = ?', (new_message, user_id))
	return get_user(user_id)

def set_privacy_settings(user_id: int, new_settings: dict) -> User:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('UPDATE users SET privacy_settings = ? WHERE id = ?', (str(new_settings), user_id))
	return get_user(user_id)

def recover_password(email: str) -> str:
	reset_token = generate_password_reset_token()
	print(f'Password reset token for {email}: {reset_token}')
	return reset_token
