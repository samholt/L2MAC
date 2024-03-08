from url_shortener import DATABASE
from user_accounts import USER_DB
from analytics import ANALYTICS_DB


def view_all_urls():
	return {'result': dict(DATABASE)}


def delete_url(short_url):
	if short_url in DATABASE:
		del DATABASE[short_url]
		return {'result': True}
	return {'result': False}


def delete_user(username):
	if username in USER_DB:
		del USER_DB[username]
		return {'result': True}
	return {'result': False}


def view_system_performance():
	return {
		'result': {
			'number_of_urls': len(DATABASE),
			'number_of_users': len(USER_DB),
			'number_of_clicks': sum(len(clicks) for clicks in ANALYTICS_DB.values())
		}
	}
