import url_shortener
import analytics
import user_accounts


# Mock database
DATABASE = url_shortener.DATABASE
ANALYTICS = analytics.analytics_data
USER_ACCOUNTS = user_accounts.UserAccounts()


# Function to view all shortened URLs
def view_all_urls():
	return DATABASE


# Function to delete any URL
def delete_url(url):
	if url in DATABASE:
		del DATABASE[url]
		return 'URL deleted successfully.'
	return 'URL not found.'


# Function to delete any user account
def delete_user(username):
	if username in USER_ACCOUNTS.users:
		USER_ACCOUNTS.users.pop(username, None)
		return 'User account deleted successfully.'
	return 'User not found.'


# Function to monitor system performance and analytics
def monitor_system():
	return ANALYTICS



