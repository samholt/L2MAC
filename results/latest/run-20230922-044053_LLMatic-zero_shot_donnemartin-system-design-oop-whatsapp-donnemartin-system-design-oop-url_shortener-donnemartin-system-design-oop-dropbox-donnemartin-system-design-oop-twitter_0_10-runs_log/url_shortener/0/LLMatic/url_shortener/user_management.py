from typing import List
from .models import User, URL

# In-memory database
DB = {}

def create_user(username: str, password: str) -> User:
	user = User(username, password)
	# Store the User object in the database
	DB.setdefault('users', []).append(user)
	return user

def edit_user(user: User, username: str, password: str) -> User:
	# Update the User object
	user.username = username
	user.password = password
	return user

def delete_user(user: User) -> None:
	# Remove the User object from the database
	DB['users'].remove(user)

def get_user_urls(user: User) -> List[URL]:
	# Retrieve all URL objects for the user from the database
	return [url for url in DB.get('urls', []) if url.user == user]
