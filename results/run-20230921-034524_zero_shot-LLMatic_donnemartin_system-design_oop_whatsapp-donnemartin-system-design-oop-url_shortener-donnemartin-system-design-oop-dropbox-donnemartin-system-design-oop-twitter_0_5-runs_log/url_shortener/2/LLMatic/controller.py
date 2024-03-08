class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def shorten_url(self):
		original_url, expiration_date = self.view.input_url()
		short_url = self.model.generate_short_url(original_url, expiration_date)
		self.view.display_short_url(short_url)

	def redirect_url(self, short_url):
		original_url = self.model.get_original_url(short_url)
		if original_url:
			self.model.track_click(short_url)
			self.view.redirect(short_url)
		else:
			self.view.display_error("The URL does not exist or has expired.")

	def delete_expired_urls(self):
		self.model.delete_expired_urls()
