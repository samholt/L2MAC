import datetime

# Mock database
analytics_db = {}

def record_click(short_url, ip):
	"""Record a click for a specific short URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	# Record click
	analytics_db[short_url].append({
		'date_time': datetime.datetime.now(),
		'ip': ip
	})

def get_analytics(short_url):
	"""Retrieve the analytics for a specific short URL."""
	return analytics_db.get(short_url, [])
