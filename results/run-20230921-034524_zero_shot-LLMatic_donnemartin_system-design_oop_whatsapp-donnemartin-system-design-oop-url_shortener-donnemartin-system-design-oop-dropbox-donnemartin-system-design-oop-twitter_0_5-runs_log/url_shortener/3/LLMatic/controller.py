import model
import view


class Controller:
	def __init__(self):
		self.model = model.URLDatabase()
		self.view = view.View()

	def create_short_url(self):
		long_url = self.view.get_long_url()
		short_url = self.generate_short_url()
		custom_url = self.view.get_custom_url()
		url = model.URL(long_url, short_url, custom_url)
		self.model.add_url(url)
		self.view.display_short_url(short_url)

	def generate_short_url(self):
		# This is a placeholder implementation. In a real system, we would generate a unique short URL.
		return 'short_url'

	def redirect_to_long_url(self, short_url):
		url = self.model.get_url(short_url)
		if url:
			self.model.update_click_count(short_url)
			# In a real system, we would redirect to the long URL. Here, we just print it.
			print(f'Redirecting to {url.long_url}')

	def display_click_stats(self, short_url):
		url = self.model.get_url(short_url)
		if url:
			self.view.display_click_stats(url.click_count)

	def delete_expired_urls(self):
		self.model.delete_expired_urls()

