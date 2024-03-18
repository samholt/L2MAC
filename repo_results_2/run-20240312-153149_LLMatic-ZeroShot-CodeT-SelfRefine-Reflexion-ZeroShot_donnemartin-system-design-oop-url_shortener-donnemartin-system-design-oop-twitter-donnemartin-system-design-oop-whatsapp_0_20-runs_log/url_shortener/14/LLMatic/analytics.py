import datetime

# Mock database
analytics_db = {}

def track_click(short_url, ip_address):
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	analytics_db[short_url].append({
		'time': datetime.datetime.now(),
		'ip': ip_address,
		'location': 'Unknown'
	})

def get_statistics(short_url):
	return analytics_db.get(short_url, [])
