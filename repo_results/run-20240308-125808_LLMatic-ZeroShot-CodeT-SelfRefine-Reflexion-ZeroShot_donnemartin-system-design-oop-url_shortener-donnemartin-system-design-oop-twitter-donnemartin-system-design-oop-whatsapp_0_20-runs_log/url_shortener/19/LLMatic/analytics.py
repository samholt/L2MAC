from datetime import datetime
from database import Database


class Analytics:
	def __init__(self):
		self.db = Database()

	def track_url(self, url):
		analytics_data = self.db.get('analytics', url)
		if not analytics_data:
			analytics_data = {'clicks': 0, 'details': []}
		analytics_data['clicks'] += 1
		analytics_data['details'].append({'timestamp': datetime.now().isoformat()})
		self.db.insert('analytics', url, analytics_data)

	def get_url_clicks(self, url):
		analytics_data = self.db.get('analytics', url)
		if not analytics_data:
			return 0
		return analytics_data['clicks']

	def get_url_details(self, url):
		analytics_data = self.db.get('analytics', url)
		if not analytics_data:
			return []
		return analytics_data['details']
