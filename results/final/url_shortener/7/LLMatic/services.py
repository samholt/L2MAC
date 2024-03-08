import requests
import random
import string
import datetime
from models import URL, User, Click


class URLShortenerService:
	def __init__(self):
		self.url_database = {}
		self.user_database = {}

	def generate_short_url(self, original_url, user, expiration_date=None, custom_short_url=None):
		# Validate the URL
		try:
			response = requests.get(original_url)
			response.raise_for_status()
		except (requests.RequestException, ValueError):
			return 'Invalid URL'

		# Generate a unique short URL
		short_url = custom_short_url
		if not short_url:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

		# Check if the short URL is already in use
		if self.url_database.get(short_url):
			return 'Short URL already in use'

		# Create a new URL object and add it to the database
		url = URL(original_url, short_url, user, expiration_date)
		self.url_database[short_url] = url

		# Add the URL to the user's list of URLs
		self.user_database[user].urls.append(url)

		return short_url

	def get_original_url(self, short_url):
		# Get the original URL for a short URL
		url = self.url_database.get(short_url)
		if url:
			# Check if the URL has expired
			if url.expiration_date and datetime.datetime.now() > url.expiration_date:
				return 'URL has expired'
			return url.original_url
		return None

	def record_click(self, short_url, timestamp, location):
		# Record a click on a URL
		self.url_database[short_url].clicks.append(Click(short_url, timestamp, location))

	def get_analytics(self, short_url):
		# Get the analytics for a URL
		url = self.url_database[short_url]
		return {
			'original_url': url.original_url,
			'short_url': url.short_url,
			'user': url.user,
			'created_at': url.created_at,
			'expiration_date': url.expiration_date,
			'clicks': [click.__dict__ for click in url.clicks]
		}

	def create_user(self, username, password):
		# Create a new user
		if username in self.user_database:
			return 'Username already taken'

		self.user_database[username] = User(username, password)
		return 'User created successfully'

	def authenticate_user(self, username, password):
		# Authenticate a user
		if username not in self.user_database or self.user_database[username].password != password:
			return 'Invalid username or password'

		return 'Authentication successful'

	def get_user_urls(self, username):
		# Get a user's URLs
		return [url.short_url for url in self.user_database[username].urls]

	def get_all_urls(self):
		# Get all URLs
		return [url.__dict__ for url in self.url_database.values()]

	def delete_url(self, short_url):
		# Delete a URL
		if short_url in self.url_database:
			del self.url_database[short_url]
			return 'URL deleted successfully'
		return 'URL not found'

	def delete_user(self, username):
		# Delete a user
		if username in self.user_database:
			del self.user_database[username]
			return 'User deleted successfully'
		return 'User not found'

