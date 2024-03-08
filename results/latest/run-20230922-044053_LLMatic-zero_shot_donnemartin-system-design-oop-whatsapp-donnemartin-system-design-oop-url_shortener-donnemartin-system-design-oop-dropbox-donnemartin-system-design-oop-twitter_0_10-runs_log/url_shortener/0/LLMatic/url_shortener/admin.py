from typing import List
from .models import User, URL

# In-memory database
DB = {}

def view_all_users() -> List[User]:
	# Retrieve all User objects from the database
	return list(DB.get('users', []))

def view_all_urls() -> List[URL]:
	# Retrieve all URL objects from the database
	return list(DB.get('urls', []))

def delete_user(user: User) -> None:
	# Remove the User object from the database
	DB['users'].remove(user)

def delete_url(url: URL) -> None:
	# Remove the URL object from the database
	DB['urls'].remove(url)
