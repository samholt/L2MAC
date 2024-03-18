import datetime

# Mock database
analytics_db = {}

def track_click(short_url, ip_address):
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	click_info = {'timestamp': datetime.datetime.now(), 'ip_address': ip_address}
	analytics_db[short_url].append(click_info)

def get_statistics(short_url):
	if short_url in analytics_db:
		return analytics_db[short_url]
	else:
		return []
