class URLView:
	def __init__(self):
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def input_long_url(self):
		long_url = input('Enter the long URL: ')
		expiry_date_str = input('Enter the expiry date (YYYY-MM-DD), leave blank if no expiry: ')
		expiry_date = None
		if expiry_date_str:
			expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d')
		custom_alias = input('Enter a custom short URL alias, leave blank for a random alias: ')
		short_url = self.controller.create_short_url(long_url, expiry_date, custom_alias)
		print(f'Short URL: {short_url}')

	def display_click_stats(self, short_url):
		clicks = self.controller.get_click_stats(short_url)
		print(f'Click stats for {short_url}: {clicks}')
