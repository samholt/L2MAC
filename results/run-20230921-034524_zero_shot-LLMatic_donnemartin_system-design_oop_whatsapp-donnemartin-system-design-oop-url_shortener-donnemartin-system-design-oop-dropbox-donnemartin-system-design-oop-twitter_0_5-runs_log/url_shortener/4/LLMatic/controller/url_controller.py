from model.url import URL
from model.url_database import URLDatabase


class URLController:
	def __init__(self, view):
		self.view = view
		self.view.set_controller(self)
		self.database = URLDatabase()

	def create_short_url(self, long_url, expiry_date, custom_alias):
		url = URL(long_url, expiry_date, custom_alias)
		self.database.add_url(url)
		return url.short_url

	def get_click_stats(self, short_url):
		url = self.database.get_url(short_url)
		if url:
			return url.clicks
		else:
			return 'URL not found'

	def redirect(self, short_url):
		url = self.database.get_url(short_url)
		if url and not url.is_expired():
			url.redirect()
			return url.original_url
		elif url and url.is_expired():
			self.database.delete_expired_urls()
			return 'URL expired'
		else:
			return 'URL not found'
