import url_shortener as us
import user_accounts as ua
import analytics as an

# Mock database
DATABASE = us.DATABASE
USER_ACCOUNTS = ua.USER_ACCOUNTS
ANALYTICS = an.analytics_db


def view_all_urls():
	return DATABASE

def delete_url(short_url):
	if short_url in DATABASE:
		DATABASE.pop(short_url)
		return 'URL deleted successfully.'
	else:
		return 'URL does not exist.'

def delete_user_account(username):
	if username in USER_ACCOUNTS.accounts:
		del USER_ACCOUNTS.accounts[username]
		return 'User account deleted successfully.'
	else:
		return 'User account does not exist.'

def view_system_performance():
	return ANALYTICS

