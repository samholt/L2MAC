import datetime

# Mock database
analytics_db = {}

def track_click(short_url, ip_address):
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	click_data = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address
	}
	analytics_db[short_url].append(click_data)


def get_click_data(short_url):
	return analytics_db.get(short_url, [])
