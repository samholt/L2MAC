import url_shortener
import user_accounts
import analytics

# Mock database
admin_db = {}

user_account = user_accounts.UserAccount()


def view_all_urls():
	return url_shortener.url_database

def delete_url(short_url):
	if short_url in url_shortener.url_database:
		del url_shortener.url_database[short_url]
		return 'URL deleted successfully.'
	else:
		return 'URL does not exist.'

def delete_user(username):
	if username in user_account.accounts:
		del user_account.accounts[username]
		return 'User deleted successfully.'
	else:
		return 'User does not exist.'

def monitor_system():
	return {
		'urls': view_all_urls(),
		'users': user_account.accounts,
		'analytics': analytics.analytics_db
	}
