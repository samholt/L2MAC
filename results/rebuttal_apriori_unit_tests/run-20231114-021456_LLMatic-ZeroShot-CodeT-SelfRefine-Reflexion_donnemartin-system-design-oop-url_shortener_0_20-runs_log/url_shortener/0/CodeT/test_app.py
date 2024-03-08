import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta
from app import User, URL, users, urls

# Helper Functions
def random_url():
	return f'https://example{randint(1000, 9999)}.com'

def random_username():
	return 'user' + ''.join(choices(string.ascii_lowercase + string.digits, k=5))

def random_slug():
	return ''.join(choices(string.ascii_lowercase + string.digits, k=8))

# Test Functions
class TestURLShorteningService:

	def test_input_url_shortening(self):
		# Test URL shortening
		pass

	def test_url_validation(self):
		# Test URL validation
		pass

	def test_unique_shortened_url(self):
		# Test uniqueness of shortened URLs
		pass

	def test_custom_short_link(self):
		# Test custom short link creation
		pass

	def test_redirection(self):
		# Test URL redirection
		pass

	def test_analytics_retrieval(self):
		# Test analytics retrieval
		pass

	def test_user_account_functions(self):
		# Test user account functions
		pass

	def test_admin_functions(self):
		# Test admin functions
		pass

	def test_url_expiration(self):
		# Test URL expiration
		pass
