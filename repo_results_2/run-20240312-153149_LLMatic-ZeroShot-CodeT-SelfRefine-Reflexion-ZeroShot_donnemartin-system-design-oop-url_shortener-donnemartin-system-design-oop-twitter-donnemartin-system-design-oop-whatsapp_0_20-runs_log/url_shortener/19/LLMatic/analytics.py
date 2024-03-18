import datetime
import random


# Mock database
analytics_db = {}


def track_click(short_url):
	"""Track a click for a given short URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	click_info = {
		'timestamp': datetime.datetime.now(),
		'location': random.choice(['USA', 'Canada', 'UK', 'Germany', 'Australia'])  # Mock location
	}

	analytics_db[short_url].append(click_info)


def get_statistics(short_url):
	"""Retrieve statistics for a given short URL."""
	return analytics_db.get(short_url, [])
