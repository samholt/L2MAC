import datetime

# Mock database
analytics_db = {}


def track_click(short_url, location):
	"""Track each click for a shortened URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	analytics_db[short_url].append({
		'time': datetime.datetime.now(),
		'location': location
	})


def get_statistics(short_url):
	"""Retrieve statistics for a shortened URL."""
	if short_url not in analytics_db:
		return None
	return {
		'clicks': len(analytics_db[short_url]),
		'details': analytics_db[short_url]
	}
