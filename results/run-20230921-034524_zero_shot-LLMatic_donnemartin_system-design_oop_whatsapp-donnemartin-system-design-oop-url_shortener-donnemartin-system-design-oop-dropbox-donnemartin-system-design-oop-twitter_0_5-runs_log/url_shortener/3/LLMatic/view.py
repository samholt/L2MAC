class View:
	def get_long_url(self):
		return input("Enter the long URL: ")

	def display_short_url(self, short_url):
		print(f"The short URL is: {short_url}")

	def get_custom_url(self):
		return input("Enter a custom URL (optional): ")

	def display_click_stats(self, click_count):
		print(f"The URL has been clicked {click_count} times.")
