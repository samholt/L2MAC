class URLShortenerView:
	def get_long_url(self):
		return input('Please enter the long URL: ')

	def display_short_url(self, short_url):
		print('The short URL is: ', short_url)

	def get_short_url(self):
		return input('Please enter the short URL: ')

	def redirect_to_long_url(self, long_url):
		print('Redirecting to original URL: ', long_url)
