class View:
	def __init__(self, controller):
		self.controller = controller

	def input_url(self):
		original_url = input("Enter the URL to be shortened: ")
		expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
		return original_url, expiration_date

	def display_short_url(self, short_url):
		print(f"The shortened URL is: {short_url}")

	def redirect(self, short_url):
		original_url = self.controller.get_original_url(short_url)
		if original_url:
			print(f"Redirecting to {original_url}")
		else:
			print("The URL does not exist or has expired.")
