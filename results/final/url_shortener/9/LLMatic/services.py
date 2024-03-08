import string
import random
from urllib.request import urlopen
from models import URL, Click, User, mock_db, mock_click_db, mock_user_db
from typing import Optional, Dict
from datetime import datetime

def generate_short_url(url: str, length: int = 5) -> str:
	characters = string.ascii_letters + string.digits
	short_url = ''.join(random.choice(characters) for _ in range(length))
	while short_url in mock_db:
		short_url = ''.join(random.choice(characters) for _ in range(length))
	return short_url

def validate_and_shorten_url(original_url: str, user: Optional[str] = None, expiration: Optional[datetime] = None) -> str:
	try:
		response = urlopen(original_url)
	except:
		return 'Invalid URL'
	short_url = generate_short_url(original_url)
	mock_db[short_url] = URL(original_url, short_url, user, expiration)
	return short_url

def get_original_url(short_url: str) -> Optional[str]:
	url = mock_db.get(short_url)
	if url and (not url.expiration or datetime.now() < url.expiration):
		return url.original_url
	return None

def record_click(short_url: str, location: str) -> int:
	click = Click(short_url, datetime.now(), location)
	mock_click_db[short_url] = mock_click_db.get(short_url, []) + [click]
	return len(mock_click_db[short_url])

def create_user(username: str, password: str) -> str:
	if username in mock_user_db:
		return 'Username already exists'
	mock_user_db[username] = User(username, password)
	return 'User created successfully'

def authenticate_user(username: str, password: str) -> bool:
	user = mock_user_db.get(username)
	if user and user.password == password:
		return True
	return False

def get_user_urls(username: str) -> Dict[str, str]:
	return {url.shortened_url: url.original_url for url in mock_db.values() if url.user == username}

def get_all_urls() -> Dict[str, str]:
	return {url.shortened_url: url.original_url for url in mock_db.values()}

def delete_url(short_url: str) -> str:
	if short_url in mock_db:
		del mock_db[short_url]
		return 'URL deleted successfully'
	return 'URL not found'

def get_all_users() -> Dict[str, str]:
	return {user.username: user.password for user in mock_user_db.values()}

def delete_user(username: str) -> str:
	if username in mock_user_db:
		del mock_user_db[username]
		return 'User deleted successfully'
	return 'User not found'
