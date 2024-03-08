import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta
import app

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
		# TODO: Implement test
		pass

	def test_url_validation(self):
		# TODO: Implement test
		pass

	def test_unique_shortened_url(self):
		# TODO: Implement test
		pass

	def test_custom_short_link(self):
		# TODO: Implement test
		pass

	def test_redirection(self):
		# TODO: Implement test
		pass

	def test_analytics_retrieval(self):
		# TODO: Implement test
		pass

	def test_user_account_functions(self):
		# TODO: Implement test
		pass

	def test_admin_functions(self):
		# TODO: Implement test
		pass

	def test_url_expiration(self):
		# TODO: Implement test
		pass
