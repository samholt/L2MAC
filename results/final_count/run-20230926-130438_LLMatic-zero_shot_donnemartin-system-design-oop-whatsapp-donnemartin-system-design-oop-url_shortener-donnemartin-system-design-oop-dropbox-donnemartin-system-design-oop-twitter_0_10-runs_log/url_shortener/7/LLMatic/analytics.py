import datetime
import pytz
from collections import defaultdict

# Mock database
analytics_db = defaultdict(list)


def track_click(short_url, location):
	"""Track a click for a given short URL."""
	timestamp = datetime.datetime.now(pytz.utc)
	analytics_db[short_url].append((timestamp, location))


def get_statistics(short_url):
	"""Retrieve statistics for a given short URL."""
	clicks = analytics_db.get(short_url, [])
	return {
		'clicks': len(clicks),
		'details': [{'timestamp': str(click[0]), 'location': click[1]} for click in clicks]
	}
