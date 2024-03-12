import datetime

# Mock database
analytics_db = {}


def track_click(short_url, ip_address):
	"""Track a click for a shortened URL.

	:param short_url: Shortened URL
	:param ip_address: IP address of the clicker
	"""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	click_data = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address
	}

	analytics_db[short_url].append(click_data)


def get_statistics(short_url):
	"""Retrieve statistics for a shortened URL.

	:param short_url: Shortened URL
	:return: List of click data
	"""
	return analytics_db.get(short_url, [])
