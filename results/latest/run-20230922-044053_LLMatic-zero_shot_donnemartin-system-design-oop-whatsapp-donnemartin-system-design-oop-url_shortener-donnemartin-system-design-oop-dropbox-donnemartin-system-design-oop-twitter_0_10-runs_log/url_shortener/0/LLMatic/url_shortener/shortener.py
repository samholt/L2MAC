import random
import string
from .models import URL, User
from datetime import datetime, timedelta

# In-memory database
DB = {}

def generate_short_code():
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def create_shortened_url(original_url: str, user: User, expires_in: timedelta = timedelta(days=30)):
	short_code = generate_short_code()
	shortened_url = f'http://short.en/{short_code}'
	expires_at = datetime.now() + expires_in
	url = URL(original_url, shortened_url, user, datetime.now(), expires_at)
	# Store the URL object in the database
	DB.setdefault('urls', []).append(url)
	return url
