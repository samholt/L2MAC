import datetime
import random

# Mock database
analytics_db = {}


def track_click(short_url):
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	
	click_info = {
		'time': datetime.datetime.now(),
		'location': random.choice(['USA', 'Canada', 'UK', 'Germany', 'Australia'])  # Mock location
	}
	
	analytics_db[short_url].append(click_info)


def get_statistics(short_url):
	if short_url not in analytics_db:
		return None
	
	return analytics_db[short_url]


def get_system_performance():
	return {'total_urls': len(analytics_db), 'total_clicks': sum(len(clicks) for clicks in analytics_db.values())}
