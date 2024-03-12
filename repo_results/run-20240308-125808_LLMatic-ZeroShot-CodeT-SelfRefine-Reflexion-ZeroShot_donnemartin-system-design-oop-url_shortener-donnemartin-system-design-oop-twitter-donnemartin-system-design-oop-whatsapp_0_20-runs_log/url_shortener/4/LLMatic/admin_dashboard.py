import url_shortener as us
import analytics as an
import user_accounts as ua

# Mock database
DATABASE = us.DATABASE
analytics_db = an.analytics_db
users = ua.UserAccounts()

users.create_account('testuser')

def get_all_urls():
	"""Retrieve all shortened URLs."""
	return DATABASE

def delete_url(short_url):
	"""Delete a URL."""
	if short_url in DATABASE:
		DATABASE.pop(short_url)
		return 'URL deleted successfully.'
	return 'URL does not exist.'

def delete_user(username):
	"""Delete a user account."""
	return users.delete_user(username)

def get_system_performance():
	"""Display system performance and analytics."""
	performance = {}
	for url in DATABASE:
		performance[url] = an.get_click_details(url)
	return performance
