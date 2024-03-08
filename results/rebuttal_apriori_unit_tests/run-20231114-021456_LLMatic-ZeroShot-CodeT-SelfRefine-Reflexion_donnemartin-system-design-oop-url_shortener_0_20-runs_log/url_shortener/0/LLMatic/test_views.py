import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta
from models import User, Admin, URL
from app import app

# Helper Functions
def random_url():
	return f"https://example{randint(1000, 9999)}.com"

def random_username():
	return 'user' + ''.join(choices(string.ascii_lowercase + string.digits, k=5))

def random_slug():
	return ''.join(choices(string.ascii_lowercase + string.digits, k=8))

# Test Functions
class TestURLShorteningService:

	def setup_method(self):
		self.client = app.test_client()

	def test_admin_functions(self):
		admin_username = random_username()
		admin_password = 'password'
		admin = Admin(admin_username, admin_password)
		Admin.save_to_db(admin)

		response = self.client.get(f'/admin/{admin_username}/all_urls')
		assert response.status_code == 200

		user_username = random_username()
		user_password = 'password'
		user = User(user_username, user_password)
		User.save_to_db(user)

		response = self.client.post(f'/admin/{admin_username}/delete_user', data={'user': user_username})
		assert response.status_code == 200

		url = random_url()
		short_url = random_slug()
		url_obj = URL(url, short_url, user, datetime.now(), datetime.now() + timedelta(days=1))
		URL.save_to_db(url_obj)

		response = self.client.post(f'/admin/{admin_username}/delete_url', data={'url': short_url})
		assert response.status_code == 200

		response = self.client.get(f'/admin/{admin_username}/system_stats')
		assert response.status_code == 200
		assert 'system_stats' in response.get_json()


