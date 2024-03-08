from model import URL, URLStore
from view import URLShortenerView


class URLShortenerController:
	def __init__(self):
		self.url_store = URLStore()
		self.view = URLShortenerView()

	def create_short_url(self):
		long_url = self.view.get_long_url()
		url = URL(long_url)
		self.url_store.add_url(url)
		self.view.display_short_url(url.short_url)

	def redirect_to_long_url(self):
		short_url = self.view.get_short_url()
		url = self.url_store.get_url(short_url)
		if url and not url.is_expired():
			url.increment_clicks()
			self.view.redirect_to_long_url(url.original_url)
		else:
			self.view.redirect_to_long_url('URL not found or expired.')

	def delete_expired_urls(self):
		self.url_store.delete_expired_urls()

